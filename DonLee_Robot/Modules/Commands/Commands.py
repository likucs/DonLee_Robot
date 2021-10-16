# (c) @SpEcHIDe
# (c) @AlbertEinsteinTG
# (c) @Muhammed_RK, @Mo_Tech_YT , @Mo_Tech_Group, @MT_Botz
# Copyright permission under MIT License
# All rights reserved by PR0FESS0R-99
# License -> https://github.com/PR0FESS0R-99/DonLee_Robot/blob/main/LICENSE

from pyrogram import filters, Client
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from pyrogram.errors import UserNotParticipant
from DonLee_Robot import Translation, LOGGER, Mo_Tech_YT
from DonLee_Robot.Modules.Filters import Database
from DonLee_Robot.donlee_robot import DonLee_Robot
from DonLee_Robot.Modules import DEPLOY, HEROKU
db = Database()

@DonLee_Robot.on_message(filters.command(["start"]) & filters.private, group=1)
async def start(bot, update):
    update_channel = Mo_Tech_YT.MO_TECH_YT_15
    if FORCES_SUB:
         invite_link = await bot.create_chat_invite_link(int(FORCES_SUB))
         try:
             user = await bot.get_chat_member(int(FORCES_SUB), message.from_user.id)
             if user.status == "kicked":
                 await bot.send_message(
                     chat_id=message.from_user.id,
                     text="Sorry Sir, You are Banned to use me.",
                     parse_mode="markdown",
                     disable_web_page_preview=True
                 )
                 return
        except UserNotParticipant:
            ident, file_id = message.text.split("_-_-_-_")
            await bot.send_message(
                chat_id=message.from_user.id,
                text="**🙏 Join My Main Channel 👇!**",
                reply_markup=InlineKeyboardMarkup([
                    [ InlineKeyboardButton(text=" 📢 Join My Update Channel 📢", url=invite_link.invite_link)]
              ])
            )
            return
        except Exception:
            await update.reply_text(f"<b>This bot should be the admin on your update channel</b>\n\n<b>💢 ഈ ചാനലിൽ  @{Mo_Tech_YT.MO_TECH_YT_15} ബോട്ടിനെ അഡ്മിൻ ആക്. എന്നിട്ട് /start കൊടുക്</b>\n\n<b>🗣️ any Doubt @Mo_Tech_Group</b>")
            return
    try:
        file_uid = update.command[1]
    except IndexError:
        file_uid = False
    
    if file_uid:
        file_id, file_name, file_caption, file_type = await db.get_file(file_uid)
        
        if (file_id or file_type) == None:
            return
        
        caption = file_caption if file_caption != ("" or None) else ("<code>" + file_name + "</code>")
        try:
            await update.reply_cached_media(
                file_id,
                quote=True,
                caption = caption,
                parse_mode="html",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            Mo_Tech_YT.MO_TECH_YT_02
                                (
                                    DEPLOY, url=HEROKU
                                )
                        ]
                    ]
                )
            )
        except Exception as e:
            await update.reply_text(f"<b>Error:</b>\n<code>{e}</code>", True, parse_mode="html")
            LOGGER(__name__).error(e)
        return

    buttons = [
                  [
                      Mo_Tech_YT.MO_TECH_YT_02
                          (
                              '📢Update Channel', url='t.me/Mo_Tech_YT'
                          ),
                      Mo_Tech_YT.MO_TECH_YT_02
                          (
                              '💡More Botz', url='t.me/MT_Botz'
                          )
                  ],
                  [
                      Mo_Tech_YT.MO_TECH_YT_02
                          (
                              DEPLOY, url=HEROKU
                          )
                  ],
                  [
                      Mo_Tech_YT.MO_TECH_YT_02
                          (
                              '🚶Help', callback_data='help'
                          )
                  ]           
              ]

    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.START_TEXT.format(
                update.from_user.first_name),
        reply_markup=reply_markup,
        parse_mode="html",
        reply_to_message_id=update.message_id
    )

@DonLee_Robot.on_message(filters.command(["help"]) & filters.private, group=1)
async def help(bot, update):
    buttons = [
                  [
                      Mo_Tech_YT.MO_TECH_YT_02
                          (
                              DEPLOY, url=HEROKU
                          )
                  ],
                  [   
                      Mo_Tech_YT.MO_TECH_YT_02
                          (
                              '🏡 Home', callback_data='start'
                          ),
                      Mo_Tech_YT.MO_TECH_YT_02
                          (
                              'About💡', callback_data='about'
                          )
                  ]
              ]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.HELP_TEXT,
        reply_markup=reply_markup,
        parse_mode="html",
        reply_to_message_id=update.message_id
    )


@DonLee_Robot.on_message(filters.command(["about"]) & filters.private, group=1)
async def about(bot, update):
    
    buttons = [
                  [
                      Mo_Tech_YT.MO_TECH_YT_02
                          (
                              DEPLOY, url=HEROKU
                          )
                  ],
                  [
                      Mo_Tech_YT.MO_TECH_YT_02
                          (
                              '🏠 Home', callback_data='start'
                          ),
                      Mo_Tech_YT.MO_TECH_YT_02
                          (
                              'Close ❌️', callback_data='close'
                          )
                  ]
              ]
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.ABOUT_TEXT,
        reply_markup=reply_markup,
        parse_mode="html",
        reply_to_message_id=update.message_id
    )
