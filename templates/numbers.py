


def add_new_chat(topic, content, sent_by, sent_time):
    conversation_data = {"cats": {"contents": ['Welcome to the Channel'], "sent_by": ["Admin"], "sent_time": ["now"]},
           "dogs": {"contents": ['Welcome to the Channel'], "sent_by": ["Admin"], "sent_time": ["now"]}}

    if conversation_data.get(topic) == None:
        newTopic = {topic: {"contents": ['Welcome to the Channel'], "sent_by": ["Admin"], "sent_time": ["now"]}}
        conversation_data.update(newTopic)
        conversation_data[topic]["contents"].append(content)
        conversation_data[topic]["sent_by"].append(sent_by)
        conversation_data[topic]["sent_time"].append(sent_time)
        return conversation_data

    else:
        conversation_data[topic]["contents"].append(content)
        conversation_data[topic]["sent_by"].append(sent_by)
        conversation_data[topic]["sent_time"].append(sent_time)

        return conversation_data

dct = add_new_chat("mice", "welcome", "chris", "now")


for outer_key, outer_value in dct.items():
    print(outer_key)
    for inner_key, inner_value in outer_value.items():
        print("\t", inner_key)
        for elem in inner_value:
            print("\t\t", elem)


print(dct["cats"]["contents"][0])