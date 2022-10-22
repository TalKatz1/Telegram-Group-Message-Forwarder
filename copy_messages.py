from telethon import events
from telethon.sync import TelegramClient
from configparser import ConfigParser

try:
    parser = ConfigParser()
    parser.read('config.ini')

    PHONE_NUMBER = parser.get("TELEGRAM", 'PHONE_NUMBER')
    API_ID = int(parser.get("TELEGRAM", 'API_ID'))
    API_HASH = parser.get("TELEGRAM", 'API_HASH')

    # Create the client and connect
    client = TelegramClient(PHONE_NUMBER, API_ID, API_HASH)
    client.start()

except Exception as error:
    print("Error reading file config.ini, check it and try again.\n"
          "The file content should looks like this:\n"
          "[TELEGRAM]\n"
          "API_ID = 1234567\n"
          "API_HASH = xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n"
          "PHONE_NUMBER = +972544444444")
    print(error)
    input("\nPress any key to quit")
    exit()


def get_all_groups_and_channels():
    all_groups_lst = []
    memberships = client.get_dialogs()
    for line in memberships:
        if line.is_channel or line.is_group:
            group = line.to_dict()
            group_entity = group.get('entity').to_dict()
            all_groups_lst.append({'id': group_entity.get('id'),
                                   'name': group.get('name'),
                                   'participants': group_entity.get('participants_count'),
                                   'entity': group.get('entity')})
    return all_groups_lst


def choose_groups(groups, why):
    print("YOUR GROUPS:")
    count = 1
    for group in groups:
        print(f"{count}) {group.get('name')}")
        count += 1

    selection = input(f"CHOOSE GROUPS TO {why} ! UP TO 5 GROUPS ! (e.g. 1,3,4,6): ").strip().split(",")
    chosen_groups = []

    for select in selection:
        chosen_groups.append(groups[int(select)-1])

    return chosen_groups


def send_message(entity_group, message_content):
    entity = client.get_entity(int(entity_group))
    client.send_message(entity=entity, message=message_content)


# Start flow:
all_groups_and_channels = get_all_groups_and_channels()
groups_to_follow = choose_groups(all_groups_and_channels, "FOLLOW")
groups_to_send = choose_groups(all_groups_and_channels, "SEND")

entities_to_follow = []
for group in groups_to_follow:
    entities_to_follow.append(group.get('entity'))
entities_to_send = []
for group in groups_to_send:
    entities_to_send.append(group.get('entity'))

print("\n\nStarted listening to groups...")


@client.on(events.NewMessage(chats=entities_to_follow))
async def handler(event):
    raw_message = str(event.raw_text)
    for group in groups_to_follow:
        if int(group.get('id')) == int(event.chat_id) or int("-100" + str(group.get('id'))) == int(event.chat_id):
            print(f"\nNew from {group.get('name')}:")
    print(raw_message)
    for entity_to_send in entities_to_send:
        await client.send_message(entity=entity_to_send, message=raw_message)

client.run_until_disconnected()
