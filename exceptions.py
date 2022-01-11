class SearchUser(Exception):
    def __init__(self, user, error_message='UserSearchError'):
        self._user = user
        self._error_message = error_message
        super().__init__(self._error_message)

    def __str__(self):
        return f'{self._error_message}:\nuser with id `{self._user}` not found'
