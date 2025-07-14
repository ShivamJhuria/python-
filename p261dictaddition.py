# Initial dictionary with existing student marks
marks={"ram":33,"rahul":45}
# Prompt the user to enter new data
new_data=input("Enter new data (e.g., 'devesh 30'): ")
# Split the input into name and mark
name, mark=new_data.split()
# Convert the mark to an integer
mark=int(mark)
# Add the new key-value pair to the dictionary
marks[name]=mark
# Display the updated dictionary
print(marks)