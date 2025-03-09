import streamlit as st
from datetime import datetime
from zoneinfo import ZoneInfo

# Tailwind CSS for Dark Theme
dark_theme_css = """
<style>
@import url('https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css');

body {
    background-color: #1a202c; /* Dark Gray Background */
    color: #e2e8f0; /* Light Text */
}

.stTextInput, .stSelectbox, .stMultiSelect, .stButton > button {
    background-color: #2d3748 !important; /* Darker Gray */
    color: #e2e8f0 !important; /* Light Text */
    border-radius: 8px;
    padding: 10px;
    border: 1px solid #4a5568;
}

.stButton > button:hover {
    background-color: #4a5568 !important; /* Slightly Lighter Gray */
}
</style>
"""
st.markdown(dark_theme_css, unsafe_allow_html=True)


# List of Time Zones with Emojis
Time_Zones = {
    "UTC": "🌍 UTC",
    "Asia/Karachi": "🇵🇰 Asia/Karachi",
    "America/New_York": "🗽 America/New_York",
    "Europe/London": "🇬🇧 Europe/London",
    "Asia/Tokyo": "🗾 Asia/Tokyo",
    "Australia/Sydney": "🇦🇺 Australia/Sydney",
    "Asia/Dubai": "🏜 Asia/Dubai",
    "America/Los_Angeles": "🎬 America/Los_Angeles",
    "Europe/Paris": "🇫🇷 Europe/Paris",
    "Asia/Singapore": "🇸🇬 Asia/Singapore",
    "Africa/Cairo": "🏺 Africa/Cairo",
    "Asia/Shanghai": "🏮 Asia/Shanghai",
    "America/Chicago": "🌆 America/Chicago",
    "Pacific/Honolulu": "🏝 Pacific/Honolulu",
    "America/Toronto": "🍁 America/Toronto",
    "Asia/Kolkata": "🇮🇳 Asia/Kolkata",
    "Europe/Berlin": "🇩🇪 Europe/Berlin",
    "America/Sao_Paulo": "🇧🇷 America/Sao_Paulo",
    "Africa/Lagos": "🌍 Africa/Lagos",
    "America/Mexico_City": "🌮 America/Mexico_City",
    "Australia/Melbourne": "🦘 Australia/Melbourne",
    "Asia/Bangkok": "🌴 Asia/Bangkok",
    "Asia/Seoul": "🇰🇷 Asia/Seoul",
    "America/Denver": "⛰ America/Denver",
    "Europe/Moscow": "🇷🇺 Europe/Moscow",
    "Africa/Johannesburg": "🦁 Africa/Johannesburg",
    "Asia/Kuala_Lumpur": "🇲🇾 Asia/Kuala_Lumpur",
    "America/Bogota": "☕ America/Bogota",
    "Asia/Hong_Kong": "🏙 Asia/Hong_Kong",
    "America/Argentina/Buenos_Aires": "🇦🇷 America/Buenos_Aires",
    "Europe/Rome": "🇮🇹 Europe/Rome",
    "Europe/Madrid": "🇪🇸 Europe/Madrid",
    "Asia/Manila": "🇵🇭 Asia/Manila",
    "Asia/Jakarta": "🇮🇩 Asia/Jakarta",
    "America/Phoenix": "🌵 America/Phoenix",
    "Asia/Colombo": "🇱🇰 Asia/Colombo",
    "Pacific/Auckland": "🇳🇿 Pacific/Auckland",
    "America/Vancouver": "🌲 America/Vancouver",
    "America/Anchorage": "🐻 America/Anchorage",
    "America/Montevideo": "🇺🇾 America/Montevideo",
    "Africa/Nairobi": "🐘 Africa/Nairobi",
    "Europe/Athens": "🏛 Europe/Athens",
    "Europe/Oslo": "🇳🇴 Europe/Oslo",
    "Europe/Brussels": "🇧🇪 Europe/Brussels",
    "Asia/Yangon": "🇲🇲 Asia/Yangon",
    "America/Caracas": "🇻🇪 America/Caracas",
    "Asia/Tehran": "🇮🇷 Asia/Tehran",
    "Asia/Riyadh": "🕋 Asia/Riyadh",
    "Europe/Dublin": "🍀 Europe/Dublin",
    "Europe/Amsterdam": "🇳🇱 Europe/Amsterdam",
    "America/Guatemala": "🇬🇹 America/Guatemala",
    "Asia/Beirut": "🇱🇧 Asia/Beirut",
    "Asia/Tashkent": "🇺🇿 Asia/Tashkent",
    "Asia/Ulaanbaatar": "🇲🇳 Asia/Ulaanbaatar",
    "Asia/Kathmandu": "🇳🇵 Asia/Kathmandu",
    "Europe/Warsaw": "🇵🇱 Europe/Warsaw",
    "Europe/Zurich": "🇨🇭 Europe/Zurich",
    "Asia/Dhaka": "🇧🇩 Asia/Dhaka",
    "America/Havana": "🇨🇺 America/Havana",
    "Asia/Vladivostok": "🇷🇺 Asia/Vladivostok",
    "America/Barbados": "🏝 America/Barbados",
    "Asia/Yekaterinburg": "🇷🇺 Asia/Yekaterinburg",
    "America/Managua": "🇳🇮 America/Managua",
    "Pacific/Fiji": "🏝 Pacific/Fiji",
    "Asia/Kabul": "🇦🇫 Asia/Kabul",
    "Asia/Muscat": "🏜 Asia/Muscat",
    "Asia/Damascus": "🇸🇾 Asia/Damascus",
    "Europe/Helsinki": "🇫🇮 Europe/Helsinki",
    "Europe/Stockholm": "🇸🇪 Europe/Stockholm",
    "Europe/Lisbon": "🇵🇹 Europe/Lisbon",
    "Pacific/Guam": "🇬🇺 Pacific/Guam",
    "America/Costa_Rica": "🇨🇷 America/Costa_Rica",
    "America/La_Paz": "🇧🇴 America/La_Paz",
    "Pacific/Tongatapu": "🇹🇴 Pacific/Tongatapu",
    "Asia/Novosibirsk": "🇷🇺 Asia/Novosibirsk",
    "America/El_Salvador": "🇸🇻 America/El_Salvador",
    "Europe/Vienna": "🇦🇹 Europe/Vienna",
    "Europe/Belgrade": "🇷🇸 Europe/Belgrade",
    "Europe/Sofia": "🇧🇬 Europe/Sofia",
    "Europe/Budapest": "🇭🇺 Europe/Budapest",
    "Europe/Prague": "🇨🇿 Europe/Prague",
    "Asia/Tbilisi": "🇬🇪 Asia/Tbilisi",
    "Asia/Yerevan": "🇦🇲 Asia/Yerevan",
    "Europe/Bucharest": "🇷🇴 Europe/Bucharest",
    "Asia/Ashgabat": "🇹🇲 Asia/Ashgabat",
    "Asia/Dushanbe": "🇹🇯 Asia/Dushanbe",
    "Asia/Baku": "🇦🇿 Asia/Baku",
    "Europe/Chisinau": "🇲🇩 Europe/Chisinau",
    "Asia/Ho_Chi_Minh": "🇻🇳 Asia/Ho_Chi_Minh",
    "Asia/Phnom_Penh": "🇰🇭 Asia/Phnom_Penh",
    "Asia/Vientiane": "🇱🇦 Asia/Vientiane",
    "Asia/Nicosia": "🇨🇾 Asia/Nicosia",
    "Asia/Urumqi": "🇨🇳 Asia/Urumqi",
    "Asia/Krasnoyarsk": "🇷🇺 Asia/Krasnoyarsk",
    "Asia/Irkutsk": "🇷🇺 Asia/Irkutsk",
    "Asia/Magadan": "🇷🇺 Asia/Magadan",
    "Asia/Kamchatka": "🇷🇺 Asia/Kamchatka",
    "America/Montevideo": "🇺🇾 America/Montevideo",
    "America/Asuncion": "🇵🇾 America/Asuncion",
    "America/Lima": "🇵🇪 America/Lima",
    "America/Santiago": "🇨🇱 America/Santiago",
    "America/Quito": "🇪🇨 America/Quito",
    "America/Port-au-Prince": "🇭🇹 America/Port-au-Prince",
}


# App Title with Tailwind
st.markdown("<h1 class='text-3xl font-bold text-center text-blue-400'>🌎 Time Zone App ⏳</h1>", unsafe_allow_html=True)

# Select Time Zones
selected_timezone = st.multiselect("🌍 Select Timezones", list(Time_Zones.keys()), default=["UTC", "Asia/Karachi"])

# Display current time for selected time zones
st.subheader("🕰 Selected Timezones")
for tz in selected_timezone:
    current_time = datetime.now(ZoneInfo(tz)).strftime("%Y-%m-%d %I:%M:%S %p")
    st.write(f"**{Time_Zones[tz]}**: `{current_time}`")

# Convert Time Between TimeZones
st.subheader("🔄 Convert Time Between TimeZones")
current_time = st.time_input("⏰ Current Time", value=datetime.now().time())
from_tz = st.selectbox("🕰 From Timezone", list(Time_Zones.keys()), index=0)
to_tz = st.selectbox("🌎 To Timezone", list(Time_Zones.keys()), index=1)

if st.button("🔄 Convert Time"):
    dt = datetime.combine(datetime.today(), current_time, tzinfo=ZoneInfo(from_tz))
    converted_time = dt.astimezone(ZoneInfo(to_tz)).strftime("%Y-%m-%d %I:%M:%S %p")
    st.success(f"✅ Converted Time in {Time_Zones[to_tz]}: {converted_time}")









































































# # required libary
# import streamlit as st
# from datetime import datetime
# from zoneinfo import ZoneInfo

# Time_Zones = [
#     "UTC",
#     "Asia/Karachi",
#     "America/New_York",
#     "Europe/London",
#     "Asia/Tokyo",
#     "Australia/Sydney",
#     "Asia/Dubai",
#     "America/Los_Angeles",
#     "Europe/Paris",
#     "Asia/Singapore",
#     "Africa/Cairo",
#     "Asia/Shanghai",
#     "America/Chicago",
#     "Pacific/Honolulu",
#     "America/Toronto",
#     "Asia/Kolkata",          # India Standard Time
#     "Europe/Berlin",         # Central European Time
#     "America/Sao_Paulo",     # Brazil Time
#     "Africa/Lagos",          # West Africa Time
#     "America/Mexico_City",   # Central Standard Time (Mexico)
#     "Australia/Melbourne",   # Australian Eastern Time
#     "Asia/Bangkok",          # Indochina Time
#     "Asia/Seoul",            # Korea Standard Time
#     "America/Denver",        # Mountain Time (US)
#     "Europe/Moscow",         # Moscow Standard Time
#     "Africa/Johannesburg",   # South Africa Standard Time
#     "Asia/Kuala_Lumpur",     # Malaysia Time
#     "America/Bogota",        # Colombia Time
#     "Asia/Hong_Kong",        # Hong Kong Time
#     "America/Argentina/Buenos_Aires",  # Argentina Time
#     "Europe/Rome",           # Central European Time (Italy)
#     "Europe/Madrid",         # Central European Time (Spain)
#     "Asia/Manila",           # Philippine Time
#     "Asia/Jakarta",          # Western Indonesia Time
#     "America/Phoenix",       # Mountain Standard Time (US, no DST)
#     "Asia/Colombo",          # Sri Lanka Time
#     "Pacific/Auckland",      # New Zealand Time
#     "America/Vancouver",     # Pacific Time (Canada)
#     "America/Anchorage",     # Alaska Time (US)
#     "America/Montevideo",    # Uruguay Time
#     "Africa/Nairobi",        # East Africa Time
#     "Europe/Athens",         # Eastern European Time (Greece)
#     "Europe/Oslo",           # Central European Time (Norway)
#     "Europe/Brussels",       # Central European Time (Belgium)
#     "Asia/Yangon",           # Myanmar Time
#     "America/Caracas",       # Venezuela Time
#     "Asia/Tehran",           # Iran Standard Time
#     "Asia/Riyadh",           # Arabia Standard Time
#     "Europe/Dublin",         # Irish Standard Time
#     "Europe/Amsterdam",      # Central European Time (Netherlands)
#     "America/Guatemala",     # Central America Time
#     "Asia/Beirut",           # Eastern European Time (Lebanon)
#     "Asia/Tashkent",         # Uzbekistan Time
#     "Asia/Ulaanbaatar",      # Mongolia Time
#     "Asia/Kathmandu",        # Nepal Time
#     "Europe/Warsaw",         # Central European Time (Poland)
#     "Europe/Zurich",         # Central European Time (Switzerland)
#     "Asia/Dhaka",            # Bangladesh Time
#     "America/Havana",        # Cuba Standard Time
#     "Asia/Vladivostok",      # Vladivostok Time (Russia)
#     "America/Barbados",      # Atlantic Time (Barbados)
#     "Asia/Yekaterinburg",    # Yekaterinburg Time (Russia)
#     "America/Managua",       # Nicaragua Time
#     "Pacific/Fiji",          # Fiji Time
#     "Asia/Kabul",            # Afghanistan Time
#     "Asia/Muscat",           # Oman Standard Time
#     "Asia/Damascus",         # Syria Standard Time
#     "Europe/Helsinki",       # Eastern European Time (Finland)
#     "Europe/Stockholm",      # Central European Time (Sweden)
#     "Europe/Lisbon",         # Western European Time (Portugal)
#     "Pacific/Guam",          # Chamorro Standard Time
#     "America/Costa_Rica",    # Central America Time
#     "America/La_Paz",        # Bolivia Time
#     "Pacific/Tongatapu",     # Tonga Time
#     "Asia/Novosibirsk",      # Novosibirsk Time (Russia)
#     "America/El_Salvador",   # Central America Time
# ]



# st.title("Time Zone App")

# selected_timezone = st.multiselect("Select Timezones", Time_Zones, default=["UTC", "Asia/Karachi"])
# st.subheader("Selected Timezones")

# for tz in selected_timezone:
#     current_time = datetime.now(ZoneInfo(tz)).strftime("%Y-%m-%d %I:%M:%S %p")
#     st.write(f"**{tz}**: {current_time}")

# st.subheader("Convert Time Between TimeZones")
# current_time = st.time_input("Current Time", value = datetime.now().time())

# from_tz = st.selectbox("From Timezone", Time_Zones, index=0)
# to_tz = st.selectbox("To Timezone ", Time_Zones, index=1)

# if st.button("Convert Time"):
#     dt = datetime.combine(datetime.today(), current_time, tzinfo=ZoneInfo(from_tz))
#     converted_time = dt.astimezone(ZoneInfo(to_tz)).strftime("%Y-%m-%d %I:%M:%S %p")
#     st.success(f"Converted Time in {to_tz}: {converted_time}")
