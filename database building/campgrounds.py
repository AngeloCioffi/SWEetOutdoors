import requests

base_url = "https://ridb.recreation.gov/api/v1/facilities/?apikey=871320D83EEA46098DAA776A31288331&activity=9"
facilities_json = requests.get(base_url).json()
num_facilities = facilities_json["METADATA"]["RESULTS"]["TOTAL_COUNT"]
# print(num_facilities)
facility_offset = 0
while facility_offset < num_facilities:
    facilities_json = requests.get(base_url + "&offfset=" + str(facility_offset)).json()
    for facility in facilities_json["RECDATA"]:
        name = facility["FacilityName"]
        description = facility["FacilityDescription"]
        cost = facility["FacilityUseFeeDescription"]
        latitude = facility["FacilityLatitude"]
        longitude = facility["FacilityLongitude"]
        accessibilty = facility["FacilityAdaAccess"]
        reservation_url = facility["FacilityReservationURL"]
        email = facility["FacilityEmail"]
        facility_id = facility["FacilityID"]

        location_json = requests.get("https://maps.googleapis.com/maps/api/geocode/json?latlng=" + str(latitude) + "," + str(longitude) + "&key=AIzaSyD6F3rB8GtFapIpn9YG-GmqW_aGisnY5s8").json()
        # print("https://maps.googleapis.com/maps/api/geocode/json?latlng=" + str(latitude) + "," + str(longitude) + "&key=AIzaSyDzR-G-zjIEn4_YUalebfRGvdW2DszBQKg")
        for comp in location_json["results"][0]["address_components"]:
            if(comp["types"][0] == "administrative_area_level_1"):
                state = comp["long_name"]
            elif(comp["types"][0] == "postal_code"):
                zipcode = comp["long_name"]

        # campgroundInstance = Campground(name, description, cost, latitude, longitude, accessibility,
                 # reservation_url, email, zipcode, state)     

    # print(facility_offset)
    facility_offset += 50
