import re
def numify(alphanum):
    """
    Takes an alphanumeric  `alphanum` character such as 1k and return the integer equivalent.
    
    Args:
        alphanum (str): String to be converted.
        
    Returns:
        num (int, float): The equivalent of `alphanum` in integer or float.
        
    Raises:
        ValueError: Raised if alphanum does not match the pattern `^([0-9]*)(\s)?([kKmMbB])$`
        
    Notes:
        print(numify('2k')) // 2000
        print(numify('2 k')) // 2000
        print(numify('2m')) // 2000000
        print(numify('10     K')) 10000
        A more comprehensive usage example can be found here https://jaboadley.netlify.app 
    """
    # Check if alphanum format is valid
    pattern =  '^([0-9.]*)(\s)*([kKmMbBtT])$'
    match =  re.search(pattern, alphanum)
    if match is None:
	    raise ValueError("Invalid Input: correct format is 1k, 1K, 1 k, 1 K.")
	
    # Munge correct input
    else:
	   # Clean up trailing zeros from `num`
        def floater(result):
	        res = float(result) - int(result)
	        if res ==	0:
	            return int(result)
	        return(float(result))
        int_part = float(match.group(1))
        str_part = match.group()[-1]
        if str_part == 'k' or str_part == 'K':
	        kilofy = int_part * 1000
	        num = floater(kilofy)
	        return num
        elif str_part == 'm' or str_part == 'M':
	        milofy = int_part * 1000000
	        num = floater(milofy)
	        return num
        elif str_part == 'b' or str_part == 'B':
	        bilofy = int_part * 1000000000
	        num = floater(bilofy)
	        return num
        elif str_part == 't' or str_part == 'T':
	        trilofy = int_part * 1000000000000
	        num = floater(trilofy)
	        return num