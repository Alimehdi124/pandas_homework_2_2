import pandas as pd

work = pd.DataFrame([
    ['Aysel', 'Website', 17],
    ['Murad', 'Mobile App', 18],
    ['Nigar', 'Website', 16],
    ['Elvin', 'Database', 23],
    ['Aysel', 'Database', 14],
    ['Murad', 'Website', 10],
    ['Nigar', 'Mobile App', 22],
    ['Elvin', 'Mobile App', 15]
], columns=['Name', 'Project', 'Hours'])

employee_hours = work.groupby('Name')['Hours'].sum().sort_values(ascending=False)
project_hours = work.groupby('Project')['Hours'].sum().sort_values(ascending=False)
print(work.to_string(index=False))
print('\nHours by employee:\n', employee_hours)
print('\nHours by project:\n', project_hours)
print('\nEmployee with most hours:', employee_hours.idxmax(), employee_hours.max())
