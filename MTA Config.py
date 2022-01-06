# Vared Kardan Ketabkhaneh Haye Mored Niaz

try:
    from os import listdir , system
except:
    print("[X]: Lotfan Ketabkhaneh 'OS' Ra Ruye System Khod Nasb Konid !.")
try:
    from time import sleep
except:
    system("pip3 install time")
    from time import sleep
# - - - - - - - - - - - - - - - - - - - - - - - - - #

system("cls" or "clear")

print("\n[#] - - - - - - - - - - - MTA:SA Configer - - - - - - - - - - - - [#]\n\n  [1]: MTA Ro Nasb Kardam , Configesh Kon \n\n  [2]: MTA Ro Nasb Kardam Vali Dar Mahal Default Nist. \n\n  [3]: MTA Ro Nasb Nakardam, Download Va Configesh Kon.\n\n  [4]: Rahnamaye Nasb MTA Ro Behem Begoo.\n\n  [5]: Rahnamaye Download Game Mod Ro Behem Begoo.\n\n  [6]: Lotfan Az Barname Kharej Sho.\n\n[#] - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - [#]\n\n")

MTALoc = None

try:
    Chekonam = input("<>--<> Man Amade Hastam , Chikar Konam ? --> ")
    Chekonam = int(Chekonam)
except:
    print("Lotfan Dar Vared Kardan Maghadir Deghat Kamel Konid !.")
    Chekonam = input("\n<>--<> Man Amade Hastam , Chikar Konam ? --> ")
    Chekonam = int(Chekonam) 

# - - - - - - - - - - - - -  - - - - - - - - - - - #

if Chekonam == 1:
    
    SvName = input("\n[/]: Esm Server Shoma Ro Chi Bezaram ? --> ")
    Email = input("\n[/]: Lotfan Yek Email Vared Konid --> ")
    try:
        SvMaxPlr = int(input("\n[/]: Hade Aksar Tedad Player Ha Chand Ta Bashe ? --> "))
    except:
        print("\n[X]: Lotfan Yek Adad Vared Konid.!")
        SvMaxPlr = int(input("\n[/]: Hade Aksar Tedad Player Ha Chand Ta Bashe ? --> "))
        
    ConfTXT = f"""<config>
    <servername>{SvName}</servername>
    <owner_email_address>{Email}</owner_email_address>
    <serverip>auto</serverip>
    <serverport>22003</serverport>
    <maxplayers>{SvMaxPlr}</maxplayers>
    <httpport>22005</httpport>
    <httpdownloadurl></httpdownloadurl>
    <httpmaxconnectionsperclient>5</httpmaxconnectionsperclient>
    <httpdosthreshold>20</httpdosthreshold>
    <http_dos_exclude></http_dos_exclude>
    <allow_gta3_img_mods>none</allow_gta3_img_mods>
    <disableac></disableac>
    <enablesd></enablesd>
    <minclientversion>1.5.8-9.20927.0</minclientversion>
    <minclientversion_auto_update>2</minclientversion_auto_update>
    <recommendedclientversion></recommendedclientversion>
    <ase>1</ase>
    <donotbroadcastlan>0</donotbroadcastlan>
    <password></password>
    <bandwidth_reduction>medium</bandwidth_reduction>
    <player_sync_interval>100</player_sync_interval>
    <lightweight_sync_interval>1500</lightweight_sync_interval>
    <camera_sync_interval>500</camera_sync_interval>
    <ped_sync_interval>400</ped_sync_interval>
    <unoccupied_vehicle_sync_interval>400</unoccupied_vehicle_sync_interval>
    <keysync_mouse_sync_interval>100</keysync_mouse_sync_interval>
    <keysync_analog_sync_interval>100</keysync_analog_sync_interval>
    <bullet_sync>1</bullet_sync>
    <vehext_percent>0</vehext_percent>
    <vehext_ping_limit>150</vehext_ping_limit>
    <latency_reduction>0</latency_reduction>
    <idfile>server-id.keys</idfile>
    <logfile>logs/server.log</logfile>
    <authfile>logs/server_auth.log</authfile>
    <dbfile>logs/db.log</dbfile>
    <acl>acl.xml</acl>
    <scriptdebuglogfile>logs/scripts.log</scriptdebuglogfile>
    <scriptdebugloglevel>0</scriptdebugloglevel>
    <htmldebuglevel>0</htmldebuglevel>
    <filter_duplicate_log_lines>1</filter_duplicate_log_lines>
    <fpslimit>65</fpslimit>
    <voice>1</voice>
    <voice_samplerate>2</voice_samplerate>
    <voice_quality>10</voice_quality>
    <backup_path>backups</backup_path>
    <backup_interval>3</backup_interval>
    <backup_copies>5</backup_copies>
    <compact_internal_databases>1</compact_internal_databases>
    <crash_dump_upload>1</crash_dump_upload>
    <auth_serial_groups>Admin</auth_serial_groups>
    <auth_serial_http>1</auth_serial_http>
    <auth_serial_http_ip_exceptions>127.0.0.1</auth_serial_http_ip_exceptions>
    <database_credentials_protection>1</database_credentials_protection>
"""
    
    MTALoc = "C:\Program Files (x86)\MTA San Andreas 1.5\server"
    
    ConfLoc = MTALoc + "/mods/deathmatch/mtaserver.conf"
    
    ResLoc = MTALoc + "/mods/deathmatch/resources"
    
    Resources = listdir(ResLoc)
    
    Config = open(ConfLoc , "w")
    
    Config.write(ConfTXT)
    
    Config.close()
    
    Config = open(ConfLoc , "a")
    
    NoRes = ['[admin]' , '[gameplay]' , '[editor]' , '[gamemods]' , '[editor]' , '[web]']
    
    for Resrouce in Resources:
        if Resrouce not in NoRes:        
            Config.write(f'    <resource src="{Resrouce}" startup="1" />\n')
    
    Config.write("</config>")
    
    Config.close()
            
    print("\n[+]: MTA Shoma Ba Movafghait Config Shod ! , Ruz Khosh")
    
    sleep(3.0)
    
    exit()
    
elif Chekonam == 2:
    SvName = input("\n[/]: Esm Server Shoma Ro Chi Bezaram ? --> ")
    Email = input("\n[/]: Lotfan Yek Email Vared Konid --> ")
    try:
        SvMaxPlr = int(input("\n[/]: Hade Aksar Tedad Player Ha Chand Ta Bashe ? --> "))
    except:
        print("\n[X]: Lotfan Yek Adad Vared Konid.!")
        SvMaxPlr = int(input("\n[/]: Hade Aksar Tedad Player Ha Chand Ta Bashe ? --> "))
        
    ConfTXT = f"""<config>
    <servername>{SvName}</servername>
    <owner_email_address>{Email}</owner_email_address>
    <serverip>auto</serverip>
    <serverport>22003</serverport>
    <maxplayers>{SvMaxPlr}</maxplayers>
    <httpport>22005</httpport>
    <httpdownloadurl></httpdownloadurl>
    <httpmaxconnectionsperclient>5</httpmaxconnectionsperclient>
    <httpdosthreshold>20</httpdosthreshold>
    <http_dos_exclude></http_dos_exclude>
    <allow_gta3_img_mods>none</allow_gta3_img_mods>
    <disableac></disableac>
    <enablesd></enablesd>
    <minclientversion>1.5.8-9.20927.0</minclientversion>
    <minclientversion_auto_update>2</minclientversion_auto_update>
    <recommendedclientversion></recommendedclientversion>
    <ase>1</ase>
    <donotbroadcastlan>0</donotbroadcastlan>
    <password></password>
    <bandwidth_reduction>medium</bandwidth_reduction>
    <player_sync_interval>100</player_sync_interval>
    <lightweight_sync_interval>1500</lightweight_sync_interval>
    <camera_sync_interval>500</camera_sync_interval>
    <ped_sync_interval>400</ped_sync_interval>
    <unoccupied_vehicle_sync_interval>400</unoccupied_vehicle_sync_interval>
    <keysync_mouse_sync_interval>100</keysync_mouse_sync_interval>
    <keysync_analog_sync_interval>100</keysync_analog_sync_interval>
    <bullet_sync>1</bullet_sync>
    <vehext_percent>0</vehext_percent>
    <vehext_ping_limit>150</vehext_ping_limit>
    <latency_reduction>0</latency_reduction>
    <idfile>server-id.keys</idfile>
    <logfile>logs/server.log</logfile>
    <authfile>logs/server_auth.log</authfile>
    <dbfile>logs/db.log</dbfile>
    <acl>acl.xml</acl>
    <scriptdebuglogfile>logs/scripts.log</scriptdebuglogfile>
    <scriptdebugloglevel>0</scriptdebugloglevel>
    <htmldebuglevel>0</htmldebuglevel>
    <filter_duplicate_log_lines>1</filter_duplicate_log_lines>
    <fpslimit>65</fpslimit>
    <voice>1</voice>
    <voice_samplerate>2</voice_samplerate>
    <voice_quality>10</voice_quality>
    <backup_path>backups</backup_path>
    <backup_interval>3</backup_interval>
    <backup_copies>5</backup_copies>
    <compact_internal_databases>1</compact_internal_databases>
    <crash_dump_upload>1</crash_dump_upload>
    <auth_serial_groups>Admin</auth_serial_groups>
    <auth_serial_http>1</auth_serial_http>
    <auth_serial_http_ip_exceptions>127.0.0.1</auth_serial_http_ip_exceptions>
    <database_credentials_protection>1</database_credentials_protection>
"""
    
    print("\nExample --> C:\Program Files (x86)\MTA San Andreas 1.5\server")
    
    MTALoc = input("\n[-]: Mahal Nasb MTA Khodet Ro Be Tor Daghigh Benevis -->")
    
    ConfLoc = MTALoc + "/mods/deathmatch/mtaserver.conf"
    
    ResLoc = MTALoc + "/mods/deathmatch/resources"
    
    Resources = listdir(ResLoc)
    
    Config = open(ConfLoc , "w")
    
    Config.write(ConfTXT)
    
    Config.close()
    
    Config = open(ConfLoc , "a")
    
    NoRes = ['[admin]' , '[gameplay]' , '[editor]' , '[gamemods]' , '[editor]' , '[web]']
    
    for Resrouce in Resources:
        if Resrouce not in NoRes:        
            Config.write(f'    <resource src="{Resrouce}" startup="1" />\n')
    
    Config.write("</config>")
    
    Config.close()
    
    print("\n[+]: MTA Shoma Ba Movafghait Config Shod ! , Ruz Khosh")
    
    sleep(3.0)
    
    exit()
elif Chekonam == 3:
    print("In Baskhsh Be Zudi Ezafe Mishavad... @MesterScan")
elif Chekonam == 4:    
    print("\n<<-->> Baraye Nasb MTA Sa Marahel Zir Ra Tey Konid: \n\n [1]: Be Site MTA Sa Be Neshiani multitheftauto.com Beravid Va Ruye Dokme Download Click Konid \n\n [2]: File Download Shode Ra Baz Konid \n\n [3]: Ruye Dokme Next Click Konid , Dar Surat Nehsan Dadan Payam Ejra Ruye Yes Click Konid. \n\n [4]: Dokme I Agree Ra Bezanid \n\n [5]: Az Menu Bala Server Only Ra Entekhab Konid \n\n [6]: Mahal Nasb Ra Vared Konid , Taghir Mahal Nasb Tosiye Nmishavad \n\n [7]: Bad Az Payan Nasb Roye Finish Click Konid! \n\n [<>]: Dar Surat Niaz Be Komak Be ID: @MesterScan Dar Telegram Payam Dahid")
elif Chekonam == 5:
    print("\n[GM]: Shoma Baraye Download Game Mod Mitavanid Be Channel @SvMTA Ya @BegaMTA Dar Telegram Moraje'e Konid.")
elif Chekonam == 6:
    print("\nSakhte Shode Tavasot @MesterScan * 1/3/2022")
