
def get_pscore_pe(ratio):
	if ratio <= 12:
		# excellent : under-valued : steal 
		score = 4
	elif ratio > 12 and ratio <= 15:
		# good :   looks ok
		score = 3
	elif ratio > 15 and ratio <= 20:
		# average
		score = 2
	elif ratio > 20 and ratio <= 25:
		# poor : slightly over-valued 
		score = 1
	elif ratio > 25:
		# very poor : over-valued
		score = 0 
	return score

def get_pscore_peg(ratio):
	if ratio <= 1:
		# less than fair price
		score = 4
	elif ratio > 1:
		# expansive
		score = 0 
	return score

def get_pscore_pb(ratio):
	if ratio > 3:
		# less than fair price
		score = 0
	elif ratio > 2 and ratio <= 3:
		# ok  
		score = 1
	elif ratio > 1 and ratio <= 2:
		# good 
		score = 2
	elif ratio > 0 and ratio <= 1:
		# best 
		score = 3
	elif ratio == 0:
		# best 
		score = 4
	return score

def get_pscore_dy(ratio):
	if ratio > 4:
		score = 5
	elif ratio > 3 and ratio <= 4:
		score = 4
	elif ratio > 2 and ratio <= 3:
		score = 3
	elif ratio > 1 and ratio <= 2:
		score = 2
	elif ratio > 0 and ratio <= 1:
		score = 1
	else:
		score = 0
	return score

def get_offset_pscore(low, high, pos):
	if pos == True:
		multiplier = 1
	else:
		multiplier = -1
	offset = int(round(((high - low) * 100.0)/high))
	if offset < 10:
		score = 1
	elif offset >= 10 and offset < 25 :
		score = 2
	elif offset >= 25 and offset < 50 :
		score = 3
	elif offset >= 50:
		score = 4
	score = score * multiplier 
	return score

def get_pscore_iv(cmp, iv):
	if iv <= 0:
		score = 0
	elif iv == cmp:
		score = 1
	elif iv > cmp :
		low = cmp
		high = iv 
	        score = get_offset_pscore(low, high, pos=True)
	elif iv < cmp :
		high = cmp
		low = iv
	        score = get_offset_pscore(low, high, pos=False)
	return score

def get_pscore_graham(cmp, graham):
	if graham <= 0:
		score = 0
	elif graham == cmp:
		score = 1
	elif graham > cmp :
		low = cmp
		high = graham
	        score = get_offset_pscore(low, high, pos=True)
	elif graham < cmp :
		high = cmp
		low = graham
	        score = get_offset_pscore(low, high, pos=False)
	return score