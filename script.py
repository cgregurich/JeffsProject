import pandas as pd
from donor import Donor



def make_donor_from_row(row):
	info = {"donor_id": None,
		"fname": None,
		"lname": None,
		"num_guests": None,
		"phone": None,
		"email": None,
		"guests": []}

	headers = list(info.keys())

	# Deal with first 6 columns
	for i, col in enumerate(sheet.columns[:6]):
		info[headers[i]] = sheet.loc[row, col]

	# Deal with guest info
	guest_info = {"guest_id": None, "g_fname": None}
	guest_headers = list(guest_info.keys())
	for i, col in enumerate(sheet.columns[6:8]):
		guest_info[guest_headers[i]] = sheet.loc[row, col]

	info["guests"].append(guest_info)
	d = Donor(info)
	return d


def make_donor_id_guest_dicts(all_rows):
	id_set = set()
	donor_guests_dict = {}
	for donor in all_rows:
		if donor.donor_id not in id_set:
			id_set.add(donor.donor_id)
			donor_guests_dict[donor.donor_id] = [guest_dict for guest_dict in donor.guests]
		else:
			for guest_dict in donor.guests:
				donor_guests_dict[donor.donor_id].append(guest_dict)
	return donor_guests_dict

def make_donor_id_donor_obj_dict(all_rows):
	id_set = set()
	id_donors_dict = {}
	for donor in all_rows:
		if donor.donor_id not in id_set:
			id_set.add(donor.donor_id)
			id_donors_dict[donor.donor_id] = donor
	return id_donors_dict


def fix_duplicates(all_rows):
	donors_set = []
	donor_guests_dict = make_donor_id_guest_dicts(all_rows)
	id_donors_dict = make_donor_id_donor_obj_dict(all_rows)
	# make a dict of donors by IDs, where it's key:value, ID:<donor obj>
	for donor_id in id_donors_dict.keys():
		id_donors_dict[donor_id].clear_guests()
		id_donors_dict[donor_id].add_guests(donor_guests_dict[donor_id])
	return list(id_donors_dict.values())






data = pd.ExcelFile("input.xlsx", engine="openpyxl")
sheet = data.parse("Sheet1")

all_rows = []

for i in range(len(sheet)):
	all_rows.append(make_donor_from_row(i))

donors = fix_duplicates(all_rows)



for donor in donors:
	print(donor)



