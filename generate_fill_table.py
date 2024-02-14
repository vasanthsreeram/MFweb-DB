from sqlalchemy import Column,String, Integer, create_engine, Table, MetaData, delete
from sqlalchemy.sql import insert
import sqlalchemy as db
import numpy as np
from datetime import datetime

# Example: Generating a current timestamp in YYYYMMDDHHMMSS format
current_timestamp = datetime.now().strftime("%Y%m%d%H%M%S")

# Define the database connection details
username = "gridgame"
password = "J35pZyjo9kLQjh"
server = "clic.database.windows.net"
database = "clic"

db_uri = f"mssql+pymssql://{username}:{password}@{server}/{database}"
engine     = create_engine(db_uri, echo = True)
metadata   = db.MetaData()
print("Connecting to the database.")
connection = engine.connect()
print("Connected to the database.")


# Define the table schema
tasks_table = Table('task', metadata,
    Column('id', Integer, primary_key=True),
    Column('user_id', Integer),
    Column('date', String),
    # Add other columns as needed...
)

# Create the table in the database if it does not exist
metadata.create_all(engine)
def clear_table(table_name):
    try:
        table = Table(table_name, metadata, autoload_with=engine)
        connection.execute(delete(table))
        print(f"Table {table_name} cleared.")
    except Exception as e:
        print(f"Failed to clear table {table_name}: {e}")


def apple_params(user):
    n_cond = 2
    items_per_cond = 100  # will be doubled
    meanA_mean = [5, 7]
    meanA_var = 0.7
    meanB_var = [1, 2]  # Tree B with respect to tree A
    meanC_var = [1, 2]  # Tree C with respect to tree A or B
    meanD_var = [-1, -1]  # Tree D with respect to tree A
    SD = 0.8
    inf_bound = 2
    sup_bound = 10

    # Generate means for Tree A
    means_A = np.round(np.random.randn(items_per_cond) * meanA_var * 2 - meanA_var + np.mean(meanA_mean))
    means_A = np.clip(means_A, inf_bound + 2, sup_bound - 1)

    # Generate means for Tree B
    tmp_B = np.concatenate([
        np.repeat(meanB_var[0], items_per_cond // 4),
        np.repeat(-meanB_var[0], items_per_cond // 4),
        np.repeat(meanB_var[1], items_per_cond // 4),
        np.repeat(-meanB_var[1], items_per_cond // 4)
    ])
    np.random.shuffle(tmp_B)
    means_B = means_A + tmp_B
    means_B = np.clip(means_B, inf_bound + 1, sup_bound)

    # Adjust generation of tmp_C to ensure it matches the size of means_A and means_B
    tmp_C = np.concatenate([
        np.repeat(meanC_var[0], items_per_cond // 4),
        np.repeat(-meanC_var[0], items_per_cond // 4),
        np.repeat(meanC_var[1], items_per_cond // 4),
        np.repeat(-meanC_var[1], items_per_cond // 4)
    ])
    np.random.shuffle(tmp_C)
    means_C = means_A + tmp_C  # Adjust operation based on desired logic
    means_C = np.clip(means_C, inf_bound + 1, sup_bound)

    # Generate means for Tree D with corrected sizes
    means_D = np.minimum(means_A, np.minimum(means_B, means_C)) + np.random.choice(meanD_var, items_per_cond)
    means_D = np.clip(means_D, inf_bound, sup_bound)

    # Structure for further use
    task_means = np.vstack((means_A, means_B, means_C, means_D)).T

    user['task'] = {'means': task_means}
    return user

def apple_params_training(user):
    n_items = user['params']['n_training_trials']
    mean1 = 8
    mean2 = 3
    SD = 0.8
    inf_bound = 2
    sup_bound = 10

    # Generating sequences for Tree 1 and Tree 2
    means = np.array([[mean1] * n_items, [mean2] * n_items])
    training_means = means.T  # Transpose to match the MATLAB structure

    sequences = {}
    for t in range(n_items):
        for tree in range(2):
            r = training_means[t, tree] + SD * np.random.randn(4)
            r = np.round(np.clip(r, inf_bound, sup_bound))
            sequences.setdefault(t, {}).update({tree: r})

    user['training'] = {'sequences': sequences}
    return user

def general_params(ID):
    user = {
        'ID': ID,
        'params': {
            'wd': '/path/to/working/directory',
            'matlab': 'MATLAB_Version',  # You might not need this in Python
            'date': current_timestamp,  # Use Python's datetime for actual value
            'n_blocks': 4,
            'n_trialPB': 100,
            'n_training_trials': 10,
        }
    }
    return user


def prepare_task_data(user):
    # Example: Transforming task means into a list of dicts for DB insertion
    task_data = []
    for means in user['task']['means']:
        task_entry = {
            'user_id': user['ID'],
            'date': user['params']['date'],
            'means_A': means[0],
            'means_B': means[1],
            'means_C': means[2],
            'means_D': means[3],
        }
        task_data.append(task_entry)
    return task_data

def prepare_training_data(user):
    # Example: Preparing training sequences for DB insertion
    training_data = []
    for trial_id, sequences in user['training']['sequences'].items():
        for tree, seq in sequences.items():
            training_entry = {
                'user_id': user['ID'],
                'trial_id': trial_id,
                'tree': tree,
                'sequence': seq,  # Assuming your DB can store this as a list or JSON
            }
            training_data.append(training_entry)
    return training_data



def insert_data_to_db(user_data, table_name):
    table = Table(table_name, metadata, autoload_with=engine)

    connection.execute(insert(table), user_data)
def simulate_insert_data(user_data, table_name):
    print(f"\nSimulated Insertion into '{table_name}' Table:")
    for data in user_data:
        print(data)
def main():
    Nb = 100  # Example: Number of users

    for ID in range(1, Nb + 1):
        user = general_params(ID)
        user = apple_params(user)
        user = apple_params_training(user)
        
        # Prepare data for insertion
        task_data = prepare_task_data(user)
        training_data = prepare_training_data(user)
        
        # Simulate insertion into the database
        simulate_insert_data(task_data, 'task')  # 'task' is your table name
        simulate_insert_data(training_data, 'training')  # 'training' is your table name

    print("\nSimulation complete. No actual database operations were performed.")

# def main():
#     Nb = 100  # Example: Number of users
#     clear_table('task')
#     clear_table('training')

#     for ID in range(1, Nb + 1):
#         user = general_params(ID)
#         user = apple_params(user)
#         user = apple_params_training(user)
        
#         # Prepare data for insertion
#         task_data = prepare_task_data(user)
#         training_data = prepare_training_data(user)
        
#         # Insert into the database
#         insert_data_to_db(task_data, 'task')  # Assuming 'tasks' is your table name
#         insert_data_to_db(training_data, 'training')  # Assuming 'trainings' is your table name

#     # Ensure to close the connection when done
#     connection.close()


main()
