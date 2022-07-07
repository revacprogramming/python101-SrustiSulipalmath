# Databases
# https://www.py4e.com/lessons/database

def patch_music(self, notification=False):

        ''' Patch the music database to silence the rescan prompt.
        '''
        if kodi_version() < 18:
            LOG.info("version not supported for patching music db.")
            return

        with self.library.database_lock:
            with Database('music') as musicdb:
                self.library.kodi_media['Music'](musicdb.cursor).disable_rescan(musicdb.path.split('MyMusic')[1].split('.db')[0], 0)
        
        settings('MusicRescan.bool', True)

        if notification:
            dialog("notification", heading="{emby}", message=_('task_success'), icon="{emby}", time=1000, sound=False) 