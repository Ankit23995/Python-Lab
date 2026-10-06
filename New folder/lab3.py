import json

file_path = r"E:\projects\New folder\election_result.json"

with open(file_path, "r", encoding="utf-8") as file_obj:
    election_data = json.load(file_obj)

header = list(election_data[0].keys())

total_vote = 0
for caster_data in election_data:
    vote_recieved = caster_data.get("TotalVoteReceived")

    total_vote = total_vote + vote_recieved

average_vote = total_vote / len(election_data)
print(total_vote)
print(average_vote)

winning_vote = 0
winner_info = None

for winner_voter in election_data:
    if winner_voter["TotalVoteReceived"] > winning_vote:
        winning_vote = winner_voter["TotalVoteReceived"]
        winner_info = winner_voter

print(winner_info.get("CandidateName"))
print("PoliticalPartyName")
