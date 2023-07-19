import subprocess

#BASE_URL = 'https://competitions.codalab.org/competitions/'
BASE_URL = 'https://codalab.lisn.fr/competitions/'

# Clean data folder
process = subprocess.Popen('rm leaderboard_data/*'.split(), stdout=subprocess.PIPE)
output, error = process.communicate()

# Read competitions.csv
csv_location = '../data/competitions-lisn.csv'
f = open(csv_location, 'r')
rows = f.read().split('\n')
rows = rows[:-1]
f.close()

# Go through competition ID and phases ID to re-create leaderboard URLs
for row in rows:
    # title, URL, ID, phases ID
    title, url, comp_id, phases_id = row.split(';')
    comp_id = str(comp_id).replace(' ', '')
    phases_id = phases_id.split(',')
    for phase_id in phases_id:
        phase_id = str(phase_id).replace(' ', '')
        leaderboard_url = BASE_URL + comp_id + '/results/' + phase_id + '/data'
        command = 'wget ' + leaderboard_url
        print(command)
        # Download CSV
        process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
        output, error = process.communicate()
        # Rename / move CSV
        try:
            new_name = comp_id + '_' + phase_id + '.csv'
            mv_command = 'mv data leaderboard_data/' + new_name
            process = subprocess.Popen(mv_command.split(), stdout=subprocess.PIPE)
            output, error = process.communicate()
        except Exception as e:
            print('Impossible to move')

# Enjoy
