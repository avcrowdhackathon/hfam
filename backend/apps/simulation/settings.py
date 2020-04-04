# from datetime import date
#
# from .parameters import Parameters, Disposition
#
#
# def construct_parameters(request_data):
#     split_date = request_data.get("dateOfFirstHospitalizedCase", "2020-7-3").split("-")
#     association_map = {
#         "population": request_data.get("population", 10000),
#         "current_hospitalized": request_data.get("currentHospitalized", 0),
#         "market_share": request_data.get("hospitalMarketShare", 0),
#         "date_first_hospitalized": date(split_date[0], split_date[1], split_date[2]),
#         "hospitalized": Disposition(
#             request_data.get("hospitalizationPercent", 0),
#             request_data.get("averageHospitalLengthOfStay", 0)),
#         "icu": Disposition(
#             request_data.get("icuNeedPercent", 0),
#             request_data.get("averageDaysInICU", 0)),
#         "infectious_days": request_data.get("infectiousDays", 0),
#         "relative_contact_rate": request_data.get("socialDistancing", 0),
#         "ventilated": Disposition(
#             request_data.get("ventilationNeedPercent", 0),
#             request_data.get("averageDaysOnVentilator", 0)),
#         "n_days": request_data.get("numberOfDaysToProject", 100)
#     }
#     return Parameters(**association_map)
