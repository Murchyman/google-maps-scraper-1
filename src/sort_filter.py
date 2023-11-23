def sort_place(places:list, sort):
     
    def sorting_key(item):
        key = sort[0]
        value = item.get(key)

        # Handle None separately
        if value is None:
            return (0,)  # A tuple with a single element to ensure type consistency

        # Return a tuple with type indicator and value
        return (1, value) if isinstance(value, int) else (2, value)

    def sorting_bool_true(item):
        sorting_by = sort[0]
        result = item.get(sorting_by, 0)

        if result is True  or result is not None:
            return 1

        return 0

    def sorting_bool_false(item):
        sorting_by = sort[0]
        result = item.get(sorting_by, 0)

        if result is False  or result is None:
            return 1

        return 0

    sorting_order = sort[1]

    if isinstance(sorting_order, bool):
        if sorting_order:
            sorted_data = sorted(places, key=sorting_bool_false)
        else: 
            sorted_data = sorted(places, key=sorting_bool_true)
    else:
        sorted_data = sorted(places, key=sorting_key,
                         reverse=(sorting_order == "desc"))

    return sorted_data

def sort_places(places:list, sorts):
    for sort in sorts:
            places = sort_place(places, sort)

    return places


def list_contains_string(string_list, target_string):
    target_string_lower = target_string.lower()  # Convert target string to lowercase
    for item in string_list:
        if target_string_lower == item:  # Compare in a case-insensitive manner
            return True
    return False


def filter_places(places, filter_data):
    filtered_places = []
    for place in places:
        if filter_data.get("min_rating") and place.get("rating") and place["rating"] < filter_data["min_rating"]:
            continue
        if filter_data.get("max_rating") and place.get("rating") and place["rating"] > filter_data["max_rating"]:
            continue
        if filter_data.get("min_reviews") and place.get("reviews") and place["reviews"] < filter_data["min_reviews"]:
            continue
        if filter_data.get("max_reviews") and place.get("reviews") and place["reviews"] > filter_data["max_reviews"]:
            continue
        if filter_data.get("has_phone") is not None and (place.get("phone") is None) == filter_data["has_phone"]:
            continue
        if filter_data.get("has_website") is not None:
            website = place.get("website")
            if website is None or "facebook.com" in website:
                if filter_data["has_website"]:
                    continue
            elif not filter_data["has_website"]:
                continue
        if filter_data.get("category_in") and place.get("main_category") not in filter_data["category_in"]:
            continue
        filtered_places.append(place)
    return filtered_places


def sort_dict_by_keys(dictionary, keys):
    new_dict = {}
    for key in keys:
        new_dict[key] = dictionary[key]
    return new_dict
