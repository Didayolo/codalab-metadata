base_url = 'https://competitions.codalab.org/competitions/'
#base_url = 'https://codalab.lisn.upsaclay.fr/competitions/'

output = open('competitions.csv', 'w')
header = 'title; url; id; phases_id\n'
output.write(header)

for comp in Competition.objects.all():
    if comp.published: # only published competitions
        # get metadata
        title = comp.title
        title = title.replace(';', ',')
        url = base_url + str(comp.id)
        phases_id = []
        num_participants = comp.participants.count()
        num_submissions = 0
        for phase in comp.phases.all():
            phases_id.append(str(phase.id))
            num_submissions += phase.submissions.count()
        phases_id = ','.join(phases_id)
        comp_id = comp.id
        if num_participants>=5 and num_submissions>=10:
            row = '{}; {}; {}; {}\n'.format(title, url, comp_id, phases_id)
            output.write(row)
output.close()
        
# retrieve output file
#sudo docker cp django:/app/codalab/metadata.csv ./metadata.csv
        
# fields
# admins, allow_organizer_teams, allow_public_submissions, allow_teams, anonymous_leaderboard, chahub_data_hash, chahub_needs_retry, chahub_timestamp, competition_docker_image, configuration, creator, deleted, description, disallow_leaderboard_modifying, dumps, enable_detailed_results, enable_forum, enable_medical_image_viewer, enable_per_submission_metadata, enable_teams, end_date, force_submission_to_leaderboard, forum, has_registration, hide_chart, hide_top_three, id, image, image_url_base, is_migrating, is_migrating_delayed, last_modified, last_phase_migration, modified_by, original_yaml_file, pagecontainers, pages, participants, phases, published, queue, require_team_approval, reward, secret_key, show_datasets_from_yaml, start_date, submissionresultgroup, submissionscoredef, submissionscoreset, team, teams, title, url_redirect
