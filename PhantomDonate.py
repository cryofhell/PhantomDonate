
# MIT License
#
# Copyright (c) 2025 Apostol
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# Name: PhantomDonate
# Author: Apostol
# Commands:
# .dme
# scope: hikka_only
# meta developer: @cryofhell

# meta pic: https://x0.at/jhJR.jpg
# meta banner: https://x0.at/gczc.jpg

__version__ = (1, 0, 0)

from hikkatl.types import Message # type: ignore
from .. import loader

@loader.tds
class AuroraDonateMod(loader.Module):
    """Module for creating a message with your details for donations"""
    
    strings = {
        "name": "PhantomDonate",
        "cfg_custom_text": "Enter the custom message to be sent with your donation details.",
        "cfg_banner_url": "Enter the URL of the image to be sent with your donation details.",
        "cfg_CryptoBot": "Enter the URL to your multi-account in @CryptoBot.",
        "cfg_xRocket": "Enter the URL to your multi-account in @xRocket.",
    }

    strings_ru = {
        "cfg_custom_text": "Введите кастомное сообщение, которое будет отправляться с вашими реквизитами для донатов.",
        "cfg_banner_url": "Введите ссылку на изображение, которое будет отправляться с вашими реквизитами для донатов.",
        "cfg_CryptoBot": "Введите ссылку на мультисчет в @CryptoBot.",
        "cfg_xRocket": "Введите ссылку на мультисчет в @xRocket.",
    }

    strings_uz = {
        "cfg_custom_text": "Donat qilish uchun ma'lumotlaringiz bilan yuboriladigan maxsus xabarni kiriting.",
        "cfg_banner_url": "Donat qilish uchun ma'lumotlaringiz bilan yuboriladigan rasm havolasini kiriting.",
        "cfg_CryptoBot": "@CryptoBot dagi multischet havolasini kiriting.",
        "cfg_xRocket": "@xRocket dagi multischet havolasini kiriting.",
    }

    strings_de = {
        "cfg_custom_text": "Geben Sie eine benutzerdefinierte Nachricht ein, die mit Ihren Spendeninformationen gesendet wird.",
        "cfg_banner_url": "Geben Sie den Link zu einem Bild ein, das mit Ihren Spendeninformationen gesendet wird.",
        "cfg_CryptoBot": "Geben Sie den Link zu Ihrem Multikonto bei @CryptoBot ein.",
        "cfg_xRocket": "Geben Sie den Link zu Ihrem Multikonto bei @xRocket ein.",
    }

    strings_es = {
        "cfg_custom_text": "Ingrese un mensaje personalizado que se enviará con sus detalles de donación.",
        "cfg_banner_url": "Ingrese el enlace a su cuenta múltiple en @CryptoBot.",
        "cfg_xRocket": "Ingrese el enlace a su cuenta múltiple en @CryptoBot.",
    }

    def __init__(self):
        self.config = loader.ModuleConfig(
            loader.ConfigValue(
                "custom_text",
                None,
                lambda: self.strings["cfg_custom_text"],
            ),
            loader.ConfigValue(
                "banner_url",
                "https://te.legra.ph/file/a596292807cc71508b7db.jpg",
                lambda: self.strings["cfg_banner_url"],
                validator=loader.validators.Link(),
            ),
            loader.ConfigValue(
                "CryptoBot",
                None,
                lambda: self.strings["cfg_CryptoBot"],
                validator=loader.validators.Link(),
            ),
            loader.ConfigValue(
                "xRocket",
                None,
                lambda: self.strings["cfg_xRocket"],
                validator=loader.validators.Link(),
            ),
        )

    @loader.command(
        ru_doc="- Открыть реквизиты для донатов",
        uz_doc="- Donatlar uchun ma'lumotlarni ochish",
        de_doc="- Details für Spenden öffnen",
        es_doc="- Abrir detalles para donaciones",
    )
    async def dme(self, message):
        """- Open details for donations"""
        
        CryptoBot = self.config["CryptoBot"]
        xRocket = self.config["xRocket"]
        
        if self.config["custom_text"] == None:
            custom_text = "<b><i>Created by: @cryofhell</i></b>"
        else:
            custom_text = self.config["custom_text"]
            
        if self.config["banner_url"] == None:
            await self.inline.form(
                message=message,
                text=str(custom_text),
                reply_markup=[
                    [
                        {"text": "👛 CryptoBot", "url": CryptoBot},
                        {"text": "🚀 xRocket", "url": xRocket},
                    ],
                    [
                        {"text": "🔻 Закрыть", "callback": self.delete}  
                    ],
                ],
            )
        else:
            await self.inline.form(
                message=message,
                text=str(custom_text),
                photo=self.config["banner_url"],
                reply_markup=[
                    [
                        {"text": "👛 CryptoBot", "url": CryptoBot},
                        {"text": "🚀 xRocket", "url": xRocket},
                    ],
                    [
                        {"text": "🔻 Закрыть", "callback": self.delete}  
                    ],
                ],
            )

    async def delete(self, call):
        await call.delete()
