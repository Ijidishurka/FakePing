import random
import logging
from .. import loader, utils
from random import randint, choice
from asyncio import sleep

logger = logging.getLogger(__name__)


def register(cb):
    cb(fake_ping())


class fake_ping(loader.Module):
    """Подпишись на канал @modwini"""
    strings = {'name': 'fake ping v3'}

    async def pinjcmd(self, message):
        """Используй .pinj <цифры>."""
        text = utils.get_args_raw(message)
        if not text:
            await message.edit("⏱" + "<b> Скорость отклика Telegram:\n </b>" + f"<code>{random.randint(10, 600)}.{random.randint(10, 99)}</code>" + "<b> ms</b>" + " <b> \n😎 Прошло с последней  перезагрузки: </b>" + f" <b>{random.randint(10, 23)}</b>" + ":" + f"<b>{random.randint(10, 59)}</b>" + ":" + f"<b>{random.randint(10, 59)}</b>")
            return
        else:
            for pinj in ["<code>🐻 Nofin...</code>"]:
                await message.edit(pinj)
                await sleep(0.3)
            pinj = ("⏱" + "<b> Скорость отклика Telegram:\n </b>" + f"<code>{text}</code>" + "<b> ms</b>" + " <b> \n😎 Прошло с последней  перезагрузки: </b>" + f" <b>{random.randint(10, 23)}</b>" + ":" + f"<b>{random.randint(10, 59)}</b>" + ":" + f"<b>{random.randint(10, 59)}</b>")

            await message.edit(pinj)
