"""CONCATENATE(
"⬇️ ", {Created (Timezone)},
"⬇️ ", {Created By}, Space,
"⬇️", Space, {🚦 Actual Status},
" → ", {🚦 Next Status}, " ", {Do you like it or not?}, Space, Space,
IF(LEN({Details}) > 5 ,CONCATENATE("Comments: ", {Details}, Space, Space), BLANK()),
IF({Attachments}, CONCATENATE("Attachments: ", {Attachments}, Space, Space), BLANK()),
IF(LEN({Headline / Title}) > 2, CONCATENATE("Title: ", {Headline / Title}), BLANK(), Space, Space),
IF(LEN({Editing Details}) > 2, CONCATENATE("Details: ", {Editing Details}), BLANK(), Space, Space),
IF(LEN({Editor Contractor}) > 2, CONCATENATE("Editor: ", {Editor Contractor}, Space, Space), BLANK()),
IF(LEN({RAW FILES URL}) > 2, CONCATENATE("RAW Files URL: ", {RAW FILES URL}, Space, Space), BLANK()),
IF(LEN({Final Files Distribution URL}) > 2, CONCATENATE("Final Files URL: ", {Final Files Distribution URL}, Space, Space), BLANK()),
IF(LEN(Captions) > 2, CONCATENATE("Captions: ", Captions, Space, Space), BLANK()),
IF(LEN(Hashtags) > 2, CONCATENATE("Hashtags: ", Hashtags, Space, Space), BLANK()),
IF(LEN({Date Of Distribution (Timezone)}) > 2 , CONCATENATE("Distribtuion Date: ", {Date Of Distribution (Timezone)}, Space, Space), BLANK()),
IF(LEN({📲 Distribution Channels}) > 2, CONCATENATE("Distribution Channels: ",{📲 Distribution Channels},Space,Space), BLANK()),
IF({Thumbnail}, CONCATENATE("Thumbnail: ", {Thumbnail}, Space, Space, Space, Space), BLANK()), Space, Space)"""
# CONCATENATE("⬇️ ",{Created (Timezone)}," ⬇️ ",{Created By}," ⬇️",Space,Space,{🚦 Actual Status},
# " → ",{🚦 Next Status}," ",{Do you like it or not?},Space,Space,IF(LEN({Details}) > 1,
# CONCATENATE("Comments: ",{Details},Space,Space), BLANK())),"Attachments: ",{Attachments},Space,Space,
# IF(LEN({Headline / Title}) > 1, CONCATENATE("Title: ",{Headline / Title},Space,Space), BLANK())),
# IF(LEN({Editing Details}) > 1, CONCATENATE("Details: ",{Editing Details},Space,Space), BLANK())),"Editor: ",
# {Editor Contractor},Space,Space,"RAW Files URL: ",{RAW FILES URL},Space,Space,"Final Files URL: ",{
# Final Files Distribution URL},Space,Space,"Captions: ",Captions,Space,Space,"Hashtags: ",Hashtags,Space,Space,
# "Distribtuion Date: ",{Date Of Distribution (Timezone)},Space,Space,"Distribution Channels: ",
# {📲 Distribution Channels},Space,Space,"Thumbnail: ",{Thumbnail},Space,Space,Space,Space)

"""
CONCATENATE(
"⬇️ ",{Created (Timezone)},
" ⬇️ ",{Created By},
" ⬇️",Space,Space,{🚦 Actual Status}," → ",{🚦 Next Status}," ",{Do you like it or not?},Space,Space,
IF({Details}!="", "Comments: {Details}", ""
)
"""


"""CONCATENATE("⬇️ ",{Created (Timezone)},
" ⬇️ ",{Created By},
" ⬇️",Space,Space,{🚦 Actual Status},
" → ",{🚦 Next Status}," ",{Do you like it or not?},Space,Space,
IF(LEN({Details})>1,CONCATENATE("COMMENTS: ",{Details}), BLANK()),
IF({Attachments}!=BLANK(), CONCATENATE("Attachments: ",{Attachments},Space,Space), BLANK()),
IF(LEN({Headline / Title})>1,CONCATENATE("Title: ",{Headline / Title}), BLANK()),
IF(LEN({Editing Details})>1,CONCATENATE("Details: ",{Editing Details}), BLANK()),
IF({Editor Contractor}!=blank(), CONCATENATE("Editor: ",{Editor Contractor},Space,Space), BLANK()))"""


"""IF({RAW FILES URL}!=BLANK(), CONCATENATE("RAW Files URL: ",{RAW FILES URL},Space,Space), BLANK())"""








#######################################################################################################################


"""
CONCATENATE(
({🥇☑️ Editing Completed}) + ({🕹 Task Created This Month} * {🥇🕹 Task Created}) + 
({📝 Updates This Month} * {🥇📝 Updates Submitted}) + 
({⭕️ Revision This Month} * {🥇⭕️ Revision}) + 
({✍🏼 Copywriting This Month} * {🥇✍🏼 Captions Made}) + 
({✅ Posted This Month} * {🥇✅ Post Distributed}) + 
({#️⃣ Hashtags This Month} * {🥇#️⃣ Hashtags Made}) + 
({📲 Channels This Month} * {🥇📲 Channels of Distribution Added}) + 
({🔍 Editing Spell Check Review - This Month} * {🥇🔍 Spell Check Reviewed}) +
(ROUND({⏱💻 Editing Hours Editors (This Month)}, 1) * {🥇🕐 Hours Spent}) +
({👍🏼 Client Approval - All Together} * {🥇👍🏼 Client Approval})
)
"""
"""IF({Date Start Report}, 
    IF(DATETIME_FORMAT({Date Start Report}, 'YYYY-MM') = DATETIME_FORMAT(DATEADD(NOW(), "month", -1), 'YYYY-MM'), 1, 0), "")
"""



"""CONCATENATE(({🥇☑️ Editing Completed}) + 
({📝 Updates This Month} * {🥇📝 Updates Submitted}) + 
({⭕️ Revision This Month} * {🥇⭕️ Revision}) + 
({🔍 Editing Spell Check Review - This Month} * {🥇🔍 Spell Check Reviewed}) +
(ROUND({⏱💻 Editing Hours (This Month)}, 1) * {🥇🕐 Hours Spent}) +
({👍🏼 Client Approval - All Together} * {🥇👍🏼 Client Approval}))"""


# DATETIME_FORMAT({Date Report Last},"YYYY-MM")






"""CONCATENATE(({🥇☑️ Editing Completed}) + 
({📝 Updates This Month Editors} * {🥇📝 Updates Submitted}) + 
({⭕️ Revision This Month} * {🥇⭕️ Revision}) + 
({🔍 Editing Spell Check Review - This Month} * {🥇🔍 Spell Check Reviewed}) + 
(ROUND({⏱💻 Editing Hours Editors (This Month)}, 1) * {🥇🕐 Hours Spent}) +
({👍🏼 Client Approval - All Together} * {🥇👍🏼 Client Approval}))"""






########################################################################################################################
"""CONCATENATE(DATETIME_FORMAT({Date Start (Formula)},'MMDD')," - ",{Documenting Name}," - " ,{Cameraman}, " - ", {Brand (Shortcut)}," ",RECORD_ID())"""






#################################################################################



"""CONCATENATE(
({🥇☑️ Editing Completed} * {☑️ Tasks Done This Month}) + 
({📝 Updates This Month} * {🥇📝 Updates Submitted}) + 
({⭕️ Revision This Month} * {🥇⭕️ Revision}) + 
({🔍 Editing Spell Check Review - This Month} * {🥇🔍 Spell Check Reviewed}) +
{⏱💻 Editing Hours This Month Rounded } * {🥇🕐 Hours Spent}) +
({👍🏼 Client Approval - All Together} * {🥇👍🏼 Client Approval}))"""










"""CONCATENATE(
({🥇☑️ Editing Completed}) + ({💻 Created By} * {🥇🕹 Task Created}) + ({📝 Updates This Month} * {🥇📝 Updates Submitted}) + ({⭕️ Revision This Month} * {🥇⭕️ Revision}) + ({✍🏼 Copywriting This Month} * {🥇✍🏼 Captions Made}) + ({✅ Posted This Month} * {🥇✅ Post Distributed}) + ({#️⃣ Hashtags This Month} * {🥇#️⃣ Hashtags Made}) + ({📲 Channels This Month} * {🥇📲 Channels of Distribution Added}) + ({🔍 Editing Spell Check Review - This Month} * {🥇🔍 Spell Check Reviewed}) +(ROUND({⏱💻 Editing Hours (This Month)}, 1) * {🥇🕐 Hours Spent}) +({👍🏼 Client Approval - All Together} * {🥇👍🏼 Client Approval}))
"""



"""CONCATENATE(
({🥇☑️ Editing Completed} * {☑️ Tasks Done (Total)}) + 
({📝 Updates This Month} * {🥇📝 Updates Submitted}) + 
({⭕️ Revision This Month} * {🥇⭕️ Revision}) +  
(ROUND({⏱💻 Editing Hours (This Month)}, 1) * {🥇🕐 Hours Spent}) +
({👍🏼 Client Approval - All Together} * {🥇👍🏼 Client Approval})
)"""

"""CONCATENATE(ROUND(
({🥇☑️ Editing Completed} * {☑️ Tasks Done (Total)}) + 
({📝 Updates This Month} * {🥇📝 Updates Submitted}) + 
({⭕️ Revision This Month} * {🥇⭕️ Revision}) + 
({⏱💻 Editing Hours This Month Rounded } * {🥇🕐 Hours Spent}) + 
({👍🏼 Client Approval - All Together} * {🥇👍🏼 Client Approval})
)"""





"""IF(
    AND(
        {#️⃣ 📦 CCH} = 0, 
        OR(
            NOT(FIND("Posts", {Product 1 (Text Name)})), 
                NOT(FIND({Product 2 Text Name}))
                )
            ), 
            {Quantity (Manual)}, {Quantity (Product)}
    )"""

"""
IF(AND(
      FIND("Posts", {Product 1 (Text Name)}) = 0, 
          FIND("Posts", {Product 2 Text Name}) = 0
      ), 
          IF({#️⃣ 📦 CCH} = 0, {Quantity (Manual)}, {Quantity (Product)}), 0
    )"""



"""IF(
    FIND("Posts", {Product 1 Text Name}) = 0, 
        IF(
            {#️⃣ 📦 CCH} = 0, {Quantity (Manual)}, {Quantity (Product)}
        ), 0
        )"""



"""
IF({Product 2 SMM}, 
        IF(
            NOT({#️⃣ 📦 SMM - Feed - 📣✅ PD}), 
                {Quantity (Manual)}, {Quantity (Product)}
            ), 
                0)
                """

"""IF({Product 2 SMM}, IF(NOT({#️⃣ 📦 SMM - Feed - 📣✅ PD}), {Quantity (Manual)}, {#️⃣ 📦 SMM - Feed - 📣✅ PD}), 0)"""




"""
CONCATENATE(
"⬇️ ", {Created (Timezone)},
"⬇️ ", {Created By},
"⬇️", Space, Space,{🚦 Actual Status},
" → ", {🚦 Next Status}, " ", {Do you like it or not?}, Space, Space,
IF(LEN({Details}) > 5 ,CONCATENATE("Comments: ", {Details}, Space, Space), BLANK()),
IF({Attachments}, CONCATENATE("Attachments: ", {Attachments}, Space, Space), BLANK()),
IF(LEN({Headline / Title}) > 2, CONCATENATE("Title: ", {Headline / Title}), BLANK()),
IF(LEN({Editing Details}) > 2, CONCATENATE("Details: ", {Editing Details}), BLANK()),
IF(LEN({Editor Contractor}) > 2, CONCATENATE("Editor: ", {Editor Contractor}, Space, Space), BLANK()),
IF(LEN({RAW FILES URL}) > 2, CONCATENATE("RAW Files URL: ", {RAW FILES URL}, Space, Space), BLANK()),
IF(LEN({Final Files Distribution URL}) > 2, CONCATENATE("Final Files URL: ", {Final Files Distribution URL}, Space, Space), BLANK()),
IF(LEN(Captions) > 2, CONCATENATE("Captions: ", Captions, Space, Space), BLANK()),
IF(LEN(Hashtags) > 2, CONCATENATE("Hashtags: ", Hashtags, Space, Space), BLANK()),
IF(LEN({Date Of Distribution (Timezone)}) > 2 , CONCATENATE("Distribtuion Date: ", {Date Of Distribution (Timezone)}, Space, Space), BLANK()),
IF(LEN({📲 Distribution Channels}) > 2, CONCATENATE("Distribution Channels: ",{📲 Distribution Channels},Space,Space), BLANK()),
IF({Thumbnail}, CONCATENATE("Thumbnail: ", {Thumbnail}, Space, Space, Space, Space), BLANK()), 
IF({Instagram Feed URL}, CONCATENATE("Instagram: ", {Instagram Feed URL}, Space, Space), BLANK()),
IF({LinkedIn URL}, CONCATENATE("LinkedIn: ", {LinkedIn URL}, Space, Space), BLANK()),
IF({Facebook Feed URL}, CONCATENATE("LinkedIn: ", {Facebook Feed URL}, Space, Space), BLANK()),
Space, Space)



"""


# Formula for brand info

"""

CONCATENATE(
    IF(Weekly Calls - Date & Time, 
        CONCATENATE("Weekly Calls:\n", Weekly Calls - Date & Time, "\n"), 
        ""
    ),
     IF(Details, 
        CONCATENATE("Details:\n", Details, "\n"), 
        ""
    ),
    
    IF({Brand Slogan}, 
        CONCATENATE("Slogan:\n", {Brand Slogan}, "\n\n"), 
        ""
    ),
        
    IF({Brand Voice & Brand Tone}, 
        CONCATENATE("Brand Voice & Tone:\n", {Brand Voice & Brand Tone}, "\n\n"), 
        ""
    ),
            
    IF({Preferred Type Of Content}, 
        CONCATENATE("Preferences:\n", {Preferred Type Of Content}, "\n\n"), 
        ""
    ),
        
    IF({What services are you trying to sell?}, 
        CONCATENATE("Goals:\n", {What services are you trying to sell?}, "\n\n"), 
        ""
    ),
    
    IF({Who is your target audience?}, 
        CONCATENATE("Goals:\n", {Who is your target audience?}, "\n\n"), 
        ""
    ),
    
    IF({Competition}, 
        CONCATENATE("Competitors:\n", {Competition}, "\n\n"), 
        ""
    ),
    
    IF({What sets you apart from the competition?}, 
        CONCATENATE("What sets apart from the competition:\n", {What sets you apart from the competition?}, "\n\n"), 
        ""
    ),
    
    IF({References}, 
        CONCATENATE("References:\n", {References}, "\n\n"), 
        ""
    ),
    
    IF({Upcoming Events?}, 
        CONCATENATE("Upcoming Events:\n", {Upcoming Events?}, "\n\n"), 
        ""
    )
)

"""


###############################################################################
# Points Formula

"""
SUM({📝 Updates Submitted}, 
    IF({🚦 Actual Status} = OR("‎‎📝 Editing Spell Check Review", "📝 Spell Check Review"), 0, INT({🔍 Spell Check Reviewed})),
    IF({🚦 Actual Status} = OR("⭕️ Editing In Revision", "⭕️ Editing Revision Completed", "⭕️ Revision"), 0, INT({⭕️ Revision})),
    IF({Captions}, 0, INT({✍🏼 Captions Made})),
    IF({Hashtags}, 0, INT({#️⃣ Hashtags Made})),
    IF({Date Of Distribution}, 0, 1),
    IF({Documenting details}, 0, 1),
    IF({Location}, 0, 1),
    IF({Editing Details}, 0, 1),
    IF({Details}, 0, 1),
    IF({Instagram Feed URL}, 0, 1 * IF({Instagram Stories}, 0, {Instagram Stories})),
    IF({LinkedIn URL}, 0, 1),
    IF({Facebook Page Feed URL}, 0, 1),
    IF({YouTube URL}, 0, 1),
    IF({Twitter URL}, 0, 1),
    IF({LinkedIn Company Feed URL}, 0, 1),
    IF({TikTok URL}, 0, 1),
    IF({Instagram Feed URL}, 0, 1),
    IF({Instagram Feed URL}, 0, 1)
    )

"""




########################################################################################################################



"""

CONCATENATE(
    IF({Weekly Calls - Date & Time}, 
        CONCATENATE("🕒Weekly Calls🕒\n", DATETIME_FORMAT({Weekly Calls - Date & Time}, "LLLL"), "\n\n\n"), 
        ""
    ),
     IF(Details, 
        CONCATENATE("📔Details📔\n", Details, "\n\n\n"), 
        ""
    ),
    
    IF({Brand Slogan}, 
        CONCATENATE("🖤Slogan🖤\n", {Brand Slogan}, "\n\n\n"), 
        ""
    ),
        
    IF({Brand Voice & Brand Tone}, 
        CONCATENATE("💎Brand Voice & Tone💎\n", {Brand Voice & Brand Tone}, "\n\n\n"), 
        ""
    ),
            
    IF({Preferred Type Of Content}, 
        CONCATENATE("♢Preferences♢\n", {Preferred Type Of Content}, "\n\n\n"), 
        ""
    ),
        
    IF({What services are you trying to sell?}, 
        CONCATENATE("💪Goals💪\n", {What services are you trying to sell?}, "\n\n\n"), 
        ""
    ),
    
    IF({Who is your target audience?}, 
        CONCATENATE("🧏‍♂️Target Audience🧏‍♂️\n", {Who is your target audience?}, "\n\n\n"), 
        ""
    ),
    
    IF({Competition}, 
        CONCATENATE("🔴Competitors🔴\n", {Competition}, "\n\n"), 
        ""
    ),
    
    IF({What sets you apart from the competition?}, 
        CONCATENATE("💚What sets apart from the competition💚\n", {What sets you apart from the competition?}, "\n\n\n"), 
        ""
    ),
    
    IF({References}, 
        CONCATENATE("🔷References🔷\n", {References}, "\n\n\n"), 
        ""
    ),
    
    IF({Upcoming Events?}, 
        CONCATENATE("💃🏻Upcoming Events💃🏻\n", {Upcoming Events?}, "\n\n\n"), 
        ""
    ),
    
    IF({What social media profiles are you using? (Long Text)}, 
        CONCATENATE("🟢Social Media -- Created🟢\n", {What social media profiles are you using? (Long Text)}, "\n\n\n"), 
        ""
    ),
    
    IF({What social media do we have to create? (Long Text)}, 
        CONCATENATE("💗Social Media -- Have To Be Created💗\n", {What social media do we have to create? (Long Text)}, "\n\n\n"), 
        ""
    )
)

"""


########################################################################################################################


"""
CONCATENATE(
    IF({Date Start},
        DATETIME_FORMAT(SET_TIMEZONE({Date Start}, 'America/Los_Angeles'), 'M/D/Y h:mm A'), ""
    ),    
        " ⏱ ", 
    IF({Date End},
        (DATETIME_FORMAT(SET_TIMEZONE({Date End}, 'America/Los_Angeles'), 'M/D/Y h:mm A')), ""
    ),
        "\n\n📍 ",
    IF({Location},
        {Location}, ""
    )
)
"""


########################################################################################################################


"""
𝒂𝒃𝒄𝒅𝒆𝒇𝒈𝒉𝒊𝒋𝒌𝒍𝒎𝒏𝒐𝒑𝒒𝒓𝒔𝒕𝒖𝒗𝒘𝒙𝒚𝒛éèàëêù𝑨𝑩𝑪𝑫𝑬𝑭𝑮𝑯𝑰𝑱𝑲𝑳𝑴𝑵𝑶𝑷𝑸𝑹𝑺𝑻𝑼𝑽𝑾𝑿𝒀𝒁 & é “‘(- è_çà) =


CONCATENATE(
    "💚 𝑾𝑬𝑩 💚 ", IF({Web Site}, {Web Site}, "--"),
    "\n🌿 𝑳𝒊𝒏𝒌𝒕𝒓𝒆𝒆 🌿 ", IF({Linktr.ee}, {Linktr.ee}, "--"),
    "\n\n\n💗 𝑰𝑮 💗 ", IF({Instagram}, {Instagram}, "--"), 
    "\n\n\n💎 𝑭𝑩 💎 ", IF({Facebook}, {Facebook}, "--"),
    "\n💎 𝑭𝑩𝑷𝒆𝒓𝒔𝒐𝒏𝒂𝒍 💎 ", IF({Facebook Personal}, {Facebook Personal}, "--"),
    "\n\n\n🖤 𝑻𝒊𝒌𝑻𝒐𝒌 🖤 ",IF({TikTok}, {TikTok}, "--"),
    "\n\n\n❤️𝒀𝒐𝒖𝑻𝒖𝒃𝒆 ❤ ", IF({YouTube}, {YouTube}, "--"),
    "\n\n\n💙 𝑳𝒊𝒏𝒌𝒆𝒅𝑰𝒏 💙 ", IF({LinkedIn}, {LinkedIn}, "--"),
    "\n💠 𝑳𝒊𝒏𝒌𝒆𝒅𝑰𝒏 𝑪𝒐𝒎𝒑𝒂𝒏𝒚 💠 ", IF({LinkedIn Company Page}, {LinkedIn Company Page}, "--")
)


CONCATENATE(
    "𝐖𝐞𝐛 𝐒𝐢𝐭𝐞: ", IF({Web Site}, {Web Site}, "–"),
    "\n\n𝐋𝐢𝐧𝐤𝐭𝐫.𝐞𝐞: ", IF({Linktr.ee}, {Linktr.ee}),
    "\n\n𝐈𝐧𝐬𝐭𝐚𝐠𝐫𝐚𝐦: ", IF({Instagram}, {Instagram}, "–"), 
    "\n\n𝐅𝐚𝐜𝐞𝐛𝐨𝐨𝐤 𝐅𝐚𝐧 𝐏𝐚𝐠𝐞: ", IF({Facebook}, {Facebook}, "–"),
    "\n\n𝐅𝐚𝐜𝐞𝐛𝐨𝐨𝐤 𝐏𝐞𝐫𝐬𝐨𝐧𝐚𝐥: ", IF({Facebook Personal}, {Facebook Personal}, "–"),
    "\n\n𝐓𝐢𝐤𝐓𝐨𝐤: ",IF({TikTok}, {TikTok}, "–"),
    "\n\n𝐘𝐨𝐮𝐓𝐮𝐛𝐞: ", IF({YouTube}, {YouTube}, "–"),
    "\n\n𝐋𝐢𝐧𝐤𝐞𝐝𝐈𝐧: ", IF({LinkedIn}, {LinkedIn}, "–"),
    "\n\n𝐋𝐢𝐧𝐤𝐞𝐝𝐈𝐧 𝐂𝐨𝐦𝐩𝐚𝐧𝐲: ", IF({LinkedIn Company Page}, {LinkedIn Company Page}, "–"),
    "\n\n𝐁𝐞𝐡𝐚𝐧𝐜𝐞: ", IF({Behance}, {Behance}, "–"),
    "\n\n𝐓𝐰𝐢𝐭𝐭𝐞𝐫: ", IF({Twitter}, {Twitter}, "–"),
    "\n\n𝐏𝐢𝐧𝐭𝐞𝐫𝐞𝐬𝐭: ", IF({Pinterest}, {Pinterest}, "–"),
    "\n\n𝐆𝐨𝐨𝐠𝐥𝐞 𝐌𝐲 𝐁𝐮𝐬𝐢𝐧𝐞𝐬𝐬: ", IF({Google My Business}, {Google My Business}, "–"),
    "\n\n𝐀𝐧𝐜𝐡𝐨𝐫: ", IF({Anchor}, {Anchor}, "–"),
    "\n\nGoogle My Business: ", IF({Google My Business}, {Google My Business}, "–")
)



CONCATENATE(
    IF({Web Site}, 
        CONCATENATE("𝐖𝐞𝐛 𝐒𝐢𝐭𝐞: ", {Web Site}, "\n\n"), 
        ""
    ),
    
    IF({Linktr.ee}, 
        CONCATENATE("𝐋𝐢𝐧𝐤𝐭𝐫.𝐞𝐞: ", {Linktr.ee}, "\n\n"), 
        ""
    ),
    
    IF({Instagram}, 
    CONCATENATE("𝐈𝐧𝐬𝐭𝐚𝐠𝐫𝐚𝐦: ", {Instagram}, "\n\n"), 
    ""
    ), 
    
    IF({Facebook}, 
        CONCATENATE("𝐅𝐚𝐜𝐞𝐛𝐨𝐨𝐤 𝐅𝐚𝐧 𝐏𝐚𝐠𝐞: ", {Facebook}, "\n\n"), 
        ""
    ),
    
    IF({Facebook Personal}, 
        CONCATENATE("𝐅𝐚𝐜𝐞𝐛𝐨𝐨𝐤 𝐏𝐞𝐫𝐬𝐨𝐧𝐚𝐥: ", {Facebook Personal}, "\n\n"), 
        ""
    ),
    
    IF({TikTok}, 
        CONCATENATE("𝐓𝐢𝐤𝐓𝐨𝐤: ", {TikTok}, "\n\n"), 
        ""
    ),
    
    IF({YouTube}, 
        CONCATENATE("𝐘𝐨𝐮𝐓𝐮𝐛𝐞: ", {YouTube}, "\n\n"), 
        ""
    ),
    
    IF({LinkedIn}, 
        CONCATENATE("𝐋𝐢𝐧𝐤𝐞𝐝𝐈𝐧: ", {LinkedIn}, "\n\n"), 
        ""
    ),
    
    IF({LinkedIn Company Page}, 
        CONCATENATE("𝐋𝐢𝐧𝐤𝐞𝐝𝐈𝐧 𝐂𝐨𝐦𝐩𝐚𝐧𝐲: ", {LinkedIn Company Page}, "\n\n"), 
        ""
    ),
    
    IF({Behance}, 
        CONCATENATE("𝐁𝐞𝐡𝐚𝐧𝐜𝐞: ", {Behance}, "\n\n"), 
        ""
    ),
    
    IF({Twitter}, 
        CONCATENATE("𝐓𝐰𝐢𝐭𝐭𝐞𝐫: ", {Twitter}, "\n\n"), 
        ""
    ),
    
    IF({Pinterest}, 
        CONCATENATE("𝐏𝐢𝐧𝐭𝐞𝐫𝐞𝐬𝐭: ", {Pinterest}, "\n\n"), 
        ""
    ),
    
    IF({Google My Business}, 
        CONCATENATE("𝐆𝐨𝐨𝐠𝐥𝐞 𝐌𝐲 𝐁𝐮𝐬𝐢𝐧𝐞𝐬𝐬: ", {Google My Business}, "\n\n"), 
        ""
    ),
    
    IF({Anchor}, 
        CONCATENATE("𝐀𝐧𝐜𝐡𝐨𝐫: ", {Anchor}, "\n\n"), 
        ""
    )
)





"""

########################################################################################################################

"""


IF(IS_BEFORE({Date Start}}, DateF15), "Firts Part"), "Second Part")


DATEADD({Date Start}, -14, 'days')

IF(DAY({Date Start}) - 14 > 0, "Second Part", "Firts Part")


"""

########################################################################################################################


"""

CONCATENATE(
    IF(
        OR(
            {Status} = '⚙️ Upcoming Editing', 
            {Status} = '⏰ Task Description Creation',
            {Status} = '🙋🏻‍♂️ Editor Requested',
            {Status} = '👨🏻‍💻 Editor Assigned',
            {Status} = '🙅🏻‍♂️ Editor Replacement',
            {Status} = '🙋🏻‍♂️ Editor Needs Info',
            {Status} = '⁉️ Awaiting Details',
            {Status} = '⁉️ Technical Support',
            {Status} = '✏️ Headline Needed',
            {Status} = '🔆 Details Revised',
            {Status} = '👍🏼 Ready To Go',
            {Status} = '🚚 In Progress',
            {Status} = '✋🏼 On Hold',
            {Status} = '⭕️ Revision',
            {Status} = '📝 Spell Check Review',
            {Status} = '⚠️ Correction Review'
            {Status} = '🚚 Sub Tasks In Progress'
        ), "In Progress", 
        
        IF(
            OR(
                {Status} = '⚙️ Upcoming Editing', 
                {Status} = '⏰ Task Description Creation',
                {Status} = '🙋🏻‍♂️ Editor Requested',
                {Status} = '🙅🏻‍♂️ Editor Replacement',
                {Status} = '🙋🏻‍♂️ Editor Needs Info',
                {Status} = '⁉️ Awaiting Details',
                {Status} = '⁉️ Technical Support',
                {Status} = '✏️ Headline Needed',
                {Status} = '🔆 Details Revised',
                {Status} = '📝 Spell Check Review',
                {Status} = '⚠️ Correction Review'
            ), "Unnasigned",
            
                IF(
                    OR(
                        {Status} = '📦 Under Review', 
                        {Status} = '⭕️ Rev. Completed',
                        {Status} = '🦸🏻‍♀️ Final Files Review',
                        {Status} = '🚚 Sub Tasks Done',
                        {Status} = '📐 Content Planning',
                        {Status} = '#️⃣ Hashtags',
                        {Status} = '✍🏼 Copywriting',
                        {Status} = '🧑🏼‍💼 SM Manager Review',
                        {Status} = '🤴🏻 Client Attention',
                        {Status} = '🔄 Distribution Revision',
                        {Status} = '📅 Scheduling',
                        {Status} = '📅 Distribution Scheduled',
                        {Status} = '📲 Posting',
                        {Status} = '✅ Done',
                        {Status} = '🌆 Content Gallery',
                        {Status} = '☑️ Done Archived',
                        {Status} = '❌ Rejected'
                    ), "Completed",
                
                )
        )
    )
)





"""
