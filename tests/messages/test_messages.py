import os
from datetime import datetime

import approvaltests
from approvaltests import Options
from approvaltests.scrubbers import scrub_all_guids

from chatroom.model import TimeFactory

approval_options = Options().with_scrubber(scrub_all_guids)


class Test_when_sending_messages:

    def test_messages_are_stored_in_database(self, command, repository):
        command.user = "Luke Skywalker"
        command.message = "This is Red Leader. We're approaching the Ison Corridor!"
        command.execute()

        message = repository.query()[0]
        approvaltests.verify(message)

    def test_messages_are_broadcast_to_everyone(self, command, notifier):
        command.user = "Luke Skywalker"
        command.message = "This is Red Leader. We're approaching the Ison Corridor!"
        command.execute()

        approvaltests.verify(notifier.last())
