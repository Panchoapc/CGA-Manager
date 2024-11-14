# Helper function for printing creation status
def print_creation_status(item_name, created):
    if created:
        print(f"{item_name} created.")
    else:
        print(f"{item_name} already exists.")