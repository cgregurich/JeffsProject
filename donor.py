
class Donor:
	def __init__(self, info):
		"""Arg info should match the following format"""
		self.info = {"donor_id": None,
					 "fname": None,
					 "lname": None,
					 "num_guests": None,
					 "phone": None,
					 "email": None,
					 "guests": []} # guests is a list of dictionaries
		if not self.is_info_valid(info):
			raise ValueError("arg info invalid")
		self.info = info



	def is_info_valid(self, info):
		key_set = ["donor_id", "fname", "lname", "num_guests",
			"phone", "email", "guests"]
		return key_set == list(info.keys())

	def __str__(self):
		return_str = "\n"
		for key in self.info.keys():
			return_str += f"{key}: {self.info[key]}\n"
		return return_str

	def clear_guests(self):
		self.info["guests"] = []

	def add_guests(self, guest_list):
		"""Expects arg new_guests to be a list
		consisting of dicts of format:
		{"guest_id": string, "g_fname": None}"""
		if not guest_list:
			return
		for guest in guest_list:
			self.info["guests"].append(guest)

	@property
	def donor_id(self):
		return self.info["donor_id"]

	@property
	def guests(self):
		return self.info["guests"]







