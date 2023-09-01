import h5py

# Define the path to the HDF5 file
file_path = 'training_model.h5'

try:
    # Open the HDF5 file in read mode
    with h5py.File(file_path, 'r') as file:
        # List the keys (groups and datasets) in the file
        keys = list(file.keys())
        
        print("Keys in the HDF5 file:")
        for key in keys:
            print(key)
            
        # Access and work with specific datasets or groups as needed
        if 'your_dataset_name' in keys:
            dataset = file['your_dataset_name']
            data = dataset[:]
            print("\nExample data from the dataset:")
            print(data)
except FileNotFoundError:
    print(f"File '{file_path}' not found.")
except Exception as e:
    print(f"An error occurred: {str(e)}")
