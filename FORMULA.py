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
    )
)

"""




