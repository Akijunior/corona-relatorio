
def get_scenario_on_day(context):
    scenario_context = [context[0], ]

    for i in range(len(context) - 1):
        case = context[i + 1] - context[i]
        scenario_context.append(case)

    return scenario_context