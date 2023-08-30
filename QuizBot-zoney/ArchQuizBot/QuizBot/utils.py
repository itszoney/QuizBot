class Utils:
    @staticmethod
    def format_user(user):
        if user.username:
            return f"@{user.username}"
        return f"{user.first_name} {user.last_name or ''}"

    @staticmethod
    def get_user_mention(user):
        return f"[{Utils.format_user(user)}](tg://user?id={user.id})"
