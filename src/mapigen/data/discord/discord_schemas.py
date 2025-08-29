import msgspec
from typing import Optional, Any

class get_my_application_params(msgspec.Struct):
    pass

class update_my_application_params(msgspec.Struct):
    description: Optional[Any] = None
    icon: Optional[Any] = None
    cover_image: Optional[Any] = None
    team_id: Optional[Any] = None
    flags: Optional[Any] = None
    interactions_endpoint_url: Optional[Any] = None
    explicit_content_filter: Optional[Any] = None
    max_participants: Optional[Any] = None
    type: Optional[Any] = None
    tags: Optional[Any] = None
    custom_install_url: Optional[Any] = None
    install_params: Optional[Any] = None
    role_connections_verification_url: Optional[Any] = None
    integration_types_config: Optional[Any] = None

class get_application_params(msgspec.Struct):
    application_id: Optional[Any] = None

class update_application_params(msgspec.Struct):
    application_id: Optional[Any] = None
    description: Optional[Any] = None
    icon: Optional[Any] = None
    cover_image: Optional[Any] = None
    team_id: Optional[Any] = None
    flags: Optional[Any] = None
    interactions_endpoint_url: Optional[Any] = None
    explicit_content_filter: Optional[Any] = None
    max_participants: Optional[Any] = None
    type: Optional[Any] = None
    tags: Optional[Any] = None
    custom_install_url: Optional[Any] = None
    install_params: Optional[Any] = None
    role_connections_verification_url: Optional[Any] = None
    integration_types_config: Optional[Any] = None

class applications_get_activity_instance_params(msgspec.Struct):
    application_id: Optional[Any] = None
    instance_id: Optional[str] = None

class upload_application_attachment_params(msgspec.Struct):
    application_id: Optional[Any] = None
    file: Optional[Any] = None

class list_application_commands_params(msgspec.Struct):
    application_id: Optional[Any] = None
    with_localizations: Optional[bool] = None

class bulk_set_application_commands_params(msgspec.Struct):
    application_id: Optional[Any] = None

class create_application_command_params(msgspec.Struct):
    application_id: Optional[Any] = None
    name: Optional[Any] = None
    name_localizations: Optional[Any] = None
    description: Optional[Any] = None
    description_localizations: Optional[Any] = None
    options: Optional[Any] = None
    default_member_permissions: Optional[Any] = None
    dm_permission: Optional[Any] = None
    contexts: Optional[Any] = None
    integration_types: Optional[Any] = None
    handler: Optional[Any] = None
    type: Optional[Any] = None

class get_application_command_params(msgspec.Struct):
    application_id: Optional[Any] = None
    command_id: Optional[Any] = None

class delete_application_command_params(msgspec.Struct):
    application_id: Optional[Any] = None
    command_id: Optional[Any] = None

class update_application_command_params(msgspec.Struct):
    application_id: Optional[Any] = None
    command_id: Optional[Any] = None
    name: Optional[Any] = None
    name_localizations: Optional[Any] = None
    description: Optional[Any] = None
    description_localizations: Optional[Any] = None
    options: Optional[Any] = None
    default_member_permissions: Optional[Any] = None
    dm_permission: Optional[Any] = None
    contexts: Optional[Any] = None
    integration_types: Optional[Any] = None
    handler: Optional[Any] = None

class list_application_emojis_params(msgspec.Struct):
    application_id: Optional[Any] = None

class create_application_emoji_params(msgspec.Struct):
    application_id: Optional[Any] = None
    name: Optional[Any] = None
    image: Optional[Any] = None

class get_application_emoji_params(msgspec.Struct):
    application_id: Optional[Any] = None
    emoji_id: Optional[Any] = None

class delete_application_emoji_params(msgspec.Struct):
    application_id: Optional[Any] = None
    emoji_id: Optional[Any] = None

class update_application_emoji_params(msgspec.Struct):
    application_id: Optional[Any] = None
    emoji_id: Optional[Any] = None
    name: Optional[Any] = None

class get_entitlements_params(msgspec.Struct):
    application_id: Optional[Any] = None
    user_id: Optional[Any] = None
    sku_ids: Optional[Any] = None
    guild_id: Optional[Any] = None
    before: Optional[Any] = None
    after: Optional[Any] = None
    limit: Optional[int] = None
    exclude_ended: Optional[bool] = None
    exclude_deleted: Optional[bool] = None
    only_active: Optional[bool] = None

class create_entitlement_params(msgspec.Struct):
    application_id: Optional[Any] = None
    sku_id: Optional[Any] = None
    owner_type: Optional[Any] = None

class get_entitlement_params(msgspec.Struct):
    application_id: Optional[Any] = None
    entitlement_id: Optional[Any] = None

class delete_entitlement_params(msgspec.Struct):
    application_id: Optional[Any] = None
    entitlement_id: Optional[Any] = None

class consume_entitlement_params(msgspec.Struct):
    application_id: Optional[Any] = None
    entitlement_id: Optional[Any] = None

class list_guild_application_commands_params(msgspec.Struct):
    application_id: Optional[Any] = None
    guild_id: Optional[Any] = None
    with_localizations: Optional[bool] = None

class bulk_set_guild_application_commands_params(msgspec.Struct):
    application_id: Optional[Any] = None
    guild_id: Optional[Any] = None

class create_guild_application_command_params(msgspec.Struct):
    application_id: Optional[Any] = None
    guild_id: Optional[Any] = None
    name: Optional[Any] = None
    name_localizations: Optional[Any] = None
    description: Optional[Any] = None
    description_localizations: Optional[Any] = None
    options: Optional[Any] = None
    default_member_permissions: Optional[Any] = None
    dm_permission: Optional[Any] = None
    contexts: Optional[Any] = None
    integration_types: Optional[Any] = None
    handler: Optional[Any] = None
    type: Optional[Any] = None

class list_guild_application_command_permissions_params(msgspec.Struct):
    application_id: Optional[Any] = None
    guild_id: Optional[Any] = None

class get_guild_application_command_params(msgspec.Struct):
    application_id: Optional[Any] = None
    guild_id: Optional[Any] = None
    command_id: Optional[Any] = None

class delete_guild_application_command_params(msgspec.Struct):
    application_id: Optional[Any] = None
    guild_id: Optional[Any] = None
    command_id: Optional[Any] = None

class update_guild_application_command_params(msgspec.Struct):
    application_id: Optional[Any] = None
    guild_id: Optional[Any] = None
    command_id: Optional[Any] = None
    name: Optional[Any] = None
    name_localizations: Optional[Any] = None
    description: Optional[Any] = None
    description_localizations: Optional[Any] = None
    options: Optional[Any] = None
    default_member_permissions: Optional[Any] = None
    dm_permission: Optional[Any] = None
    contexts: Optional[Any] = None
    integration_types: Optional[Any] = None
    handler: Optional[Any] = None

class get_guild_application_command_permissions_params(msgspec.Struct):
    application_id: Optional[Any] = None
    guild_id: Optional[Any] = None
    command_id: Optional[Any] = None

class set_guild_application_command_permissions_params(msgspec.Struct):
    application_id: Optional[Any] = None
    guild_id: Optional[Any] = None
    command_id: Optional[Any] = None
    permissions: Optional[Any] = None

class get_application_role_connections_metadata_params(msgspec.Struct):
    application_id: Optional[Any] = None

class update_application_role_connections_metadata_params(msgspec.Struct):
    application_id: Optional[Any] = None

class get_channel_params(msgspec.Struct):
    channel_id: Optional[Any] = None

class delete_channel_params(msgspec.Struct):
    channel_id: Optional[Any] = None

class update_channel_params(msgspec.Struct):
    channel_id: Optional[Any] = None

class follow_channel_params(msgspec.Struct):
    channel_id: Optional[Any] = None
    webhook_channel_id: Optional[Any] = None

class list_channel_invites_params(msgspec.Struct):
    channel_id: Optional[Any] = None

class create_channel_invite_params(msgspec.Struct):
    channel_id: Optional[Any] = None

class list_messages_params(msgspec.Struct):
    channel_id: Optional[Any] = None
    around: Optional[Any] = None
    before: Optional[Any] = None
    after: Optional[Any] = None
    limit: Optional[int] = None

class create_message_params(msgspec.Struct):
    channel_id: Optional[Any] = None
    content: Optional[Any] = None
    embeds: Optional[Any] = None
    allowed_mentions: Optional[Any] = None
    sticker_ids: Optional[Any] = None
    components: Optional[Any] = None
    flags: Optional[Any] = None
    attachments: Optional[Any] = None
    poll: Optional[Any] = None
    shared_client_theme: Optional[Any] = None
    confetti_potion: Optional[Any] = None
    message_reference: Optional[Any] = None
    nonce: Optional[Any] = None
    enforce_nonce: Optional[Any] = None
    tts: Optional[Any] = None
    files_0: Optional[Any] = None
    files_1: Optional[Any] = None
    files_2: Optional[Any] = None
    files_3: Optional[Any] = None
    files_4: Optional[Any] = None
    files_5: Optional[Any] = None
    files_6: Optional[Any] = None
    files_7: Optional[Any] = None
    files_8: Optional[Any] = None
    files_9: Optional[Any] = None

class bulk_delete_messages_params(msgspec.Struct):
    channel_id: Optional[Any] = None
    messages: Optional[Any] = None

class list_pins_params(msgspec.Struct):
    channel_id: Optional[Any] = None
    before: Optional[str] = None
    limit: Optional[int] = None

class create_pin_params(msgspec.Struct):
    channel_id: Optional[Any] = None
    message_id: Optional[Any] = None

class delete_pin_params(msgspec.Struct):
    channel_id: Optional[Any] = None
    message_id: Optional[Any] = None

class get_message_params(msgspec.Struct):
    channel_id: Optional[Any] = None
    message_id: Optional[Any] = None

class delete_message_params(msgspec.Struct):
    channel_id: Optional[Any] = None
    message_id: Optional[Any] = None

class update_message_params(msgspec.Struct):
    channel_id: Optional[Any] = None
    message_id: Optional[Any] = None
    content: Optional[Any] = None
    embeds: Optional[Any] = None
    flags: Optional[Any] = None
    allowed_mentions: Optional[Any] = None
    sticker_ids: Optional[Any] = None
    components: Optional[Any] = None
    attachments: Optional[Any] = None
    files_0: Optional[Any] = None
    files_1: Optional[Any] = None
    files_2: Optional[Any] = None
    files_3: Optional[Any] = None
    files_4: Optional[Any] = None
    files_5: Optional[Any] = None
    files_6: Optional[Any] = None
    files_7: Optional[Any] = None
    files_8: Optional[Any] = None
    files_9: Optional[Any] = None

class crosspost_message_params(msgspec.Struct):
    channel_id: Optional[Any] = None
    message_id: Optional[Any] = None

class delete_all_message_reactions_params(msgspec.Struct):
    channel_id: Optional[Any] = None
    message_id: Optional[Any] = None

class list_message_reactions_by_emoji_params(msgspec.Struct):
    channel_id: Optional[Any] = None
    message_id: Optional[Any] = None
    emoji_name: Optional[str] = None
    after: Optional[Any] = None
    limit: Optional[int] = None
    type: Optional[Any] = None

class delete_all_message_reactions_by_emoji_params(msgspec.Struct):
    channel_id: Optional[Any] = None
    message_id: Optional[Any] = None
    emoji_name: Optional[str] = None

class add_my_message_reaction_params(msgspec.Struct):
    channel_id: Optional[Any] = None
    message_id: Optional[Any] = None
    emoji_name: Optional[str] = None

class delete_my_message_reaction_params(msgspec.Struct):
    channel_id: Optional[Any] = None
    message_id: Optional[Any] = None
    emoji_name: Optional[str] = None

class delete_user_message_reaction_params(msgspec.Struct):
    channel_id: Optional[Any] = None
    message_id: Optional[Any] = None
    emoji_name: Optional[str] = None
    user_id: Optional[Any] = None

class create_thread_from_message_params(msgspec.Struct):
    channel_id: Optional[Any] = None
    message_id: Optional[Any] = None
    name: Optional[Any] = None
    auto_archive_duration: Optional[Any] = None
    rate_limit_per_user: Optional[Any] = None

class set_channel_permission_overwrite_params(msgspec.Struct):
    channel_id: Optional[Any] = None
    overwrite_id: Optional[Any] = None
    type: Optional[Any] = None
    allow: Optional[Any] = None
    deny: Optional[Any] = None

class delete_channel_permission_overwrite_params(msgspec.Struct):
    channel_id: Optional[Any] = None
    overwrite_id: Optional[Any] = None

class deprecated_list_pins_params(msgspec.Struct):
    channel_id: Optional[Any] = None

class deprecated_create_pin_params(msgspec.Struct):
    channel_id: Optional[Any] = None
    message_id: Optional[Any] = None

class deprecated_delete_pin_params(msgspec.Struct):
    channel_id: Optional[Any] = None
    message_id: Optional[Any] = None

class get_answer_voters_params(msgspec.Struct):
    channel_id: Optional[Any] = None
    message_id: Optional[Any] = None
    answer_id: Optional[int] = None
    after: Optional[Any] = None
    limit: Optional[int] = None

class poll_expire_params(msgspec.Struct):
    channel_id: Optional[Any] = None
    message_id: Optional[Any] = None

class add_group_dm_user_params(msgspec.Struct):
    channel_id: Optional[Any] = None
    user_id: Optional[Any] = None
    access_token: Optional[Any] = None
    nick: Optional[Any] = None

class delete_group_dm_user_params(msgspec.Struct):
    channel_id: Optional[Any] = None
    user_id: Optional[Any] = None

class send_soundboard_sound_params(msgspec.Struct):
    channel_id: Optional[Any] = None
    sound_id: Optional[Any] = None
    source_guild_id: Optional[Any] = None

class list_thread_members_params(msgspec.Struct):
    channel_id: Optional[Any] = None
    with_member: Optional[bool] = None
    limit: Optional[int] = None
    after: Optional[Any] = None

class join_thread_params(msgspec.Struct):
    channel_id: Optional[Any] = None

class leave_thread_params(msgspec.Struct):
    channel_id: Optional[Any] = None

class get_thread_member_params(msgspec.Struct):
    channel_id: Optional[Any] = None
    user_id: Optional[Any] = None
    with_member: Optional[bool] = None

class add_thread_member_params(msgspec.Struct):
    channel_id: Optional[Any] = None
    user_id: Optional[Any] = None

class delete_thread_member_params(msgspec.Struct):
    channel_id: Optional[Any] = None
    user_id: Optional[Any] = None

class create_thread_params(msgspec.Struct):
    channel_id: Optional[Any] = None

class list_private_archived_threads_params(msgspec.Struct):
    channel_id: Optional[Any] = None
    before: Optional[str] = None
    limit: Optional[int] = None

class list_public_archived_threads_params(msgspec.Struct):
    channel_id: Optional[Any] = None
    before: Optional[str] = None
    limit: Optional[int] = None

class thread_search_params(msgspec.Struct):
    channel_id: Optional[Any] = None
    name: Optional[str] = None
    slop: Optional[int] = None
    min_id: Optional[Any] = None
    max_id: Optional[Any] = None
    tag: Optional[Any] = None
    tag_setting: Optional[Any] = None
    archived: Optional[bool] = None
    sort_by: Optional[Any] = None
    sort_order: Optional[Any] = None
    limit: Optional[int] = None
    offset: Optional[int] = None

class trigger_typing_indicator_params(msgspec.Struct):
    channel_id: Optional[Any] = None

class list_my_private_archived_threads_params(msgspec.Struct):
    channel_id: Optional[Any] = None
    before: Optional[Any] = None
    limit: Optional[int] = None

class list_channel_webhooks_params(msgspec.Struct):
    channel_id: Optional[Any] = None

class create_webhook_params(msgspec.Struct):
    channel_id: Optional[Any] = None
    name: Optional[Any] = None
    avatar: Optional[Any] = None

class get_gateway_params(msgspec.Struct):
    pass

class get_bot_gateway_params(msgspec.Struct):
    pass

class get_guild_template_params(msgspec.Struct):
    code: Optional[str] = None

class get_guild_params(msgspec.Struct):
    guild_id: Optional[Any] = None
    with_counts: Optional[bool] = None

class delete_guild_params(msgspec.Struct):
    guild_id: Optional[Any] = None

class update_guild_params(msgspec.Struct):
    guild_id: Optional[Any] = None
    name: Optional[Any] = None
    description: Optional[Any] = None
    region: Optional[Any] = None
    icon: Optional[Any] = None
    verification_level: Optional[Any] = None
    default_message_notifications: Optional[Any] = None
    explicit_content_filter: Optional[Any] = None
    preferred_locale: Optional[Any] = None
    afk_timeout: Optional[Any] = None
    afk_channel_id: Optional[Any] = None
    system_channel_id: Optional[Any] = None
    owner_id: Optional[Any] = None
    splash: Optional[Any] = None
    banner: Optional[Any] = None
    system_channel_flags: Optional[Any] = None
    features: Optional[Any] = None
    discovery_splash: Optional[Any] = None
    home_header: Optional[Any] = None
    rules_channel_id: Optional[Any] = None
    safety_alerts_channel_id: Optional[Any] = None
    public_updates_channel_id: Optional[Any] = None
    premium_progress_bar_enabled: Optional[Any] = None

class list_guild_audit_log_entries_params(msgspec.Struct):
    guild_id: Optional[Any] = None
    user_id: Optional[Any] = None
    target_id: Optional[Any] = None
    action_type: Optional[Any] = None
    before: Optional[Any] = None
    after: Optional[Any] = None
    limit: Optional[int] = None

class list_auto_moderation_rules_params(msgspec.Struct):
    guild_id: Optional[Any] = None

class create_auto_moderation_rule_params(msgspec.Struct):
    guild_id: Optional[Any] = None

class get_auto_moderation_rule_params(msgspec.Struct):
    guild_id: Optional[Any] = None
    rule_id: Optional[Any] = None

class delete_auto_moderation_rule_params(msgspec.Struct):
    guild_id: Optional[Any] = None
    rule_id: Optional[Any] = None

class update_auto_moderation_rule_params(msgspec.Struct):
    guild_id: Optional[Any] = None
    rule_id: Optional[Any] = None

class list_guild_bans_params(msgspec.Struct):
    guild_id: Optional[Any] = None
    limit: Optional[int] = None
    before: Optional[Any] = None
    after: Optional[Any] = None

class get_guild_ban_params(msgspec.Struct):
    guild_id: Optional[Any] = None
    user_id: Optional[Any] = None

class ban_user_from_guild_params(msgspec.Struct):
    guild_id: Optional[Any] = None
    user_id: Optional[Any] = None
    delete_message_seconds: Optional[Any] = None
    delete_message_days: Optional[Any] = None

class unban_user_from_guild_params(msgspec.Struct):
    guild_id: Optional[Any] = None
    user_id: Optional[Any] = None

class bulk_ban_users_from_guild_params(msgspec.Struct):
    guild_id: Optional[Any] = None
    user_ids: Optional[Any] = None
    delete_message_seconds: Optional[Any] = None

class list_guild_channels_params(msgspec.Struct):
    guild_id: Optional[Any] = None

class create_guild_channel_params(msgspec.Struct):
    guild_id: Optional[Any] = None
    type: Optional[Any] = None
    name: Optional[Any] = None
    position: Optional[Any] = None
    topic: Optional[Any] = None
    bitrate: Optional[Any] = None
    user_limit: Optional[Any] = None
    nsfw: Optional[Any] = None
    rate_limit_per_user: Optional[Any] = None
    parent_id: Optional[Any] = None
    permission_overwrites: Optional[Any] = None
    rtc_region: Optional[Any] = None
    video_quality_mode: Optional[Any] = None
    default_auto_archive_duration: Optional[Any] = None
    default_reaction_emoji: Optional[Any] = None
    default_thread_rate_limit_per_user: Optional[Any] = None
    default_sort_order: Optional[Any] = None
    default_forum_layout: Optional[Any] = None
    default_tag_setting: Optional[Any] = None
    available_tags: Optional[Any] = None

class bulk_update_guild_channels_params(msgspec.Struct):
    guild_id: Optional[Any] = None

class list_guild_emojis_params(msgspec.Struct):
    guild_id: Optional[Any] = None

class create_guild_emoji_params(msgspec.Struct):
    guild_id: Optional[Any] = None
    name: Optional[Any] = None
    image: Optional[Any] = None
    roles: Optional[Any] = None

class get_guild_emoji_params(msgspec.Struct):
    guild_id: Optional[Any] = None
    emoji_id: Optional[Any] = None

class delete_guild_emoji_params(msgspec.Struct):
    guild_id: Optional[Any] = None
    emoji_id: Optional[Any] = None

class update_guild_emoji_params(msgspec.Struct):
    guild_id: Optional[Any] = None
    emoji_id: Optional[Any] = None
    name: Optional[Any] = None
    roles: Optional[Any] = None

class list_guild_integrations_params(msgspec.Struct):
    guild_id: Optional[Any] = None

class delete_guild_integration_params(msgspec.Struct):
    guild_id: Optional[Any] = None
    integration_id: Optional[Any] = None

class list_guild_invites_params(msgspec.Struct):
    guild_id: Optional[Any] = None

class list_guild_members_params(msgspec.Struct):
    guild_id: Optional[Any] = None
    limit: Optional[int] = None
    after: Optional[int] = None

class update_my_guild_member_params(msgspec.Struct):
    guild_id: Optional[Any] = None
    nick: Optional[Any] = None

class search_guild_members_params(msgspec.Struct):
    guild_id: Optional[Any] = None
    limit: Optional[int] = None
    query: Optional[str] = None

class get_guild_member_params(msgspec.Struct):
    guild_id: Optional[Any] = None
    user_id: Optional[Any] = None

class add_guild_member_params(msgspec.Struct):
    guild_id: Optional[Any] = None
    user_id: Optional[Any] = None
    nick: Optional[Any] = None
    roles: Optional[Any] = None
    mute: Optional[Any] = None
    deaf: Optional[Any] = None
    access_token: Optional[Any] = None
    flags: Optional[Any] = None

class delete_guild_member_params(msgspec.Struct):
    guild_id: Optional[Any] = None
    user_id: Optional[Any] = None

class update_guild_member_params(msgspec.Struct):
    guild_id: Optional[Any] = None
    user_id: Optional[Any] = None
    nick: Optional[Any] = None
    roles: Optional[Any] = None
    mute: Optional[Any] = None
    deaf: Optional[Any] = None
    channel_id: Optional[Any] = None
    communication_disabled_until: Optional[Any] = None
    flags: Optional[Any] = None

class add_guild_member_role_params(msgspec.Struct):
    guild_id: Optional[Any] = None
    user_id: Optional[Any] = None
    role_id: Optional[Any] = None

class delete_guild_member_role_params(msgspec.Struct):
    guild_id: Optional[Any] = None
    user_id: Optional[Any] = None
    role_id: Optional[Any] = None

class set_guild_mfa_level_params(msgspec.Struct):
    guild_id: Optional[Any] = None
    level: Optional[Any] = None

class get_guild_new_member_welcome_params(msgspec.Struct):
    guild_id: Optional[Any] = None

class get_guilds_onboarding_params(msgspec.Struct):
    guild_id: Optional[Any] = None

class put_guilds_onboarding_params(msgspec.Struct):
    guild_id: Optional[Any] = None
    prompts: Optional[Any] = None
    enabled: Optional[Any] = None
    default_channel_ids: Optional[Any] = None
    mode: Optional[Any] = None

class get_guild_preview_params(msgspec.Struct):
    guild_id: Optional[Any] = None

class preview_prune_guild_params(msgspec.Struct):
    guild_id: Optional[Any] = None
    days: Optional[int] = None
    include_roles: Optional[Any] = None

class prune_guild_params(msgspec.Struct):
    guild_id: Optional[Any] = None
    days: Optional[Any] = None
    compute_prune_count: Optional[Any] = None
    include_roles: Optional[Any] = None

class list_guild_voice_regions_params(msgspec.Struct):
    guild_id: Optional[Any] = None

class list_guild_roles_params(msgspec.Struct):
    guild_id: Optional[Any] = None

class create_guild_role_params(msgspec.Struct):
    guild_id: Optional[Any] = None
    name: Optional[Any] = None
    permissions: Optional[Any] = None
    color: Optional[Any] = None
    hoist: Optional[Any] = None
    mentionable: Optional[Any] = None
    icon: Optional[Any] = None
    unicode_emoji: Optional[Any] = None

class bulk_update_guild_roles_params(msgspec.Struct):
    guild_id: Optional[Any] = None

class get_guild_role_params(msgspec.Struct):
    guild_id: Optional[Any] = None
    role_id: Optional[Any] = None

class delete_guild_role_params(msgspec.Struct):
    guild_id: Optional[Any] = None
    role_id: Optional[Any] = None

class update_guild_role_params(msgspec.Struct):
    guild_id: Optional[Any] = None
    role_id: Optional[Any] = None
    name: Optional[Any] = None
    permissions: Optional[Any] = None
    color: Optional[Any] = None
    hoist: Optional[Any] = None
    mentionable: Optional[Any] = None
    icon: Optional[Any] = None
    unicode_emoji: Optional[Any] = None

class list_guild_scheduled_events_params(msgspec.Struct):
    guild_id: Optional[Any] = None
    with_user_count: Optional[bool] = None

class create_guild_scheduled_event_params(msgspec.Struct):
    guild_id: Optional[Any] = None

class get_guild_scheduled_event_params(msgspec.Struct):
    guild_id: Optional[Any] = None
    guild_scheduled_event_id: Optional[Any] = None
    with_user_count: Optional[bool] = None

class delete_guild_scheduled_event_params(msgspec.Struct):
    guild_id: Optional[Any] = None
    guild_scheduled_event_id: Optional[Any] = None

class update_guild_scheduled_event_params(msgspec.Struct):
    guild_id: Optional[Any] = None
    guild_scheduled_event_id: Optional[Any] = None

class list_guild_scheduled_event_users_params(msgspec.Struct):
    guild_id: Optional[Any] = None
    guild_scheduled_event_id: Optional[Any] = None
    with_member: Optional[bool] = None
    limit: Optional[int] = None
    before: Optional[Any] = None
    after: Optional[Any] = None

class list_guild_soundboard_sounds_params(msgspec.Struct):
    guild_id: Optional[Any] = None

class create_guild_soundboard_sound_params(msgspec.Struct):
    guild_id: Optional[Any] = None
    name: Optional[Any] = None
    volume: Optional[Any] = None
    emoji_id: Optional[Any] = None
    emoji_name: Optional[Any] = None
    sound: Optional[Any] = None

class get_guild_soundboard_sound_params(msgspec.Struct):
    guild_id: Optional[Any] = None
    sound_id: Optional[Any] = None

class delete_guild_soundboard_sound_params(msgspec.Struct):
    guild_id: Optional[Any] = None
    sound_id: Optional[Any] = None

class update_guild_soundboard_sound_params(msgspec.Struct):
    guild_id: Optional[Any] = None
    sound_id: Optional[Any] = None
    name: Optional[Any] = None
    volume: Optional[Any] = None
    emoji_id: Optional[Any] = None
    emoji_name: Optional[Any] = None

class list_guild_stickers_params(msgspec.Struct):
    guild_id: Optional[Any] = None

class create_guild_sticker_params(msgspec.Struct):
    guild_id: Optional[Any] = None
    name: Optional[Any] = None
    tags: Optional[Any] = None
    description: Optional[Any] = None
    file: Optional[Any] = None

class get_guild_sticker_params(msgspec.Struct):
    guild_id: Optional[Any] = None
    sticker_id: Optional[Any] = None

class delete_guild_sticker_params(msgspec.Struct):
    guild_id: Optional[Any] = None
    sticker_id: Optional[Any] = None

class update_guild_sticker_params(msgspec.Struct):
    guild_id: Optional[Any] = None
    sticker_id: Optional[Any] = None
    name: Optional[Any] = None
    tags: Optional[Any] = None
    description: Optional[Any] = None

class list_guild_templates_params(msgspec.Struct):
    guild_id: Optional[Any] = None

class create_guild_template_params(msgspec.Struct):
    guild_id: Optional[Any] = None
    name: Optional[Any] = None
    description: Optional[Any] = None

class sync_guild_template_params(msgspec.Struct):
    guild_id: Optional[Any] = None
    code: Optional[str] = None

class delete_guild_template_params(msgspec.Struct):
    guild_id: Optional[Any] = None
    code: Optional[str] = None

class update_guild_template_params(msgspec.Struct):
    guild_id: Optional[Any] = None
    code: Optional[str] = None
    name: Optional[Any] = None
    description: Optional[Any] = None

class get_active_guild_threads_params(msgspec.Struct):
    guild_id: Optional[Any] = None

class get_guild_vanity_url_params(msgspec.Struct):
    guild_id: Optional[Any] = None

class get_self_voice_state_params(msgspec.Struct):
    guild_id: Optional[Any] = None

class update_self_voice_state_params(msgspec.Struct):
    guild_id: Optional[Any] = None
    request_to_speak_timestamp: Optional[Any] = None
    suppress: Optional[Any] = None
    channel_id: Optional[Any] = None

class get_voice_state_params(msgspec.Struct):
    guild_id: Optional[Any] = None
    user_id: Optional[Any] = None

class update_voice_state_params(msgspec.Struct):
    guild_id: Optional[Any] = None
    user_id: Optional[Any] = None
    suppress: Optional[Any] = None
    channel_id: Optional[Any] = None

class get_guild_webhooks_params(msgspec.Struct):
    guild_id: Optional[Any] = None

class get_guild_welcome_screen_params(msgspec.Struct):
    guild_id: Optional[Any] = None

class update_guild_welcome_screen_params(msgspec.Struct):
    guild_id: Optional[Any] = None
    description: Optional[Any] = None
    welcome_channels: Optional[Any] = None
    enabled: Optional[Any] = None

class get_guild_widget_settings_params(msgspec.Struct):
    guild_id: Optional[Any] = None

class update_guild_widget_settings_params(msgspec.Struct):
    guild_id: Optional[Any] = None
    channel_id: Optional[Any] = None
    enabled: Optional[Any] = None

class get_guild_widget_params(msgspec.Struct):
    guild_id: Optional[Any] = None

class get_guild_widget_png_params(msgspec.Struct):
    guild_id: Optional[Any] = None
    style: Optional[Any] = None

class create_interaction_response_params(msgspec.Struct):
    interaction_id: Optional[Any] = None
    interaction_token: Optional[str] = None
    with_response: Optional[bool] = None

class invite_resolve_params(msgspec.Struct):
    code: Optional[str] = None
    with_counts: Optional[bool] = None
    guild_scheduled_event_id: Optional[Any] = None

class invite_revoke_params(msgspec.Struct):
    code: Optional[str] = None

class create_or_join_lobby_params(msgspec.Struct):
    idle_timeout_seconds: Optional[Any] = None
    lobby_metadata: Optional[Any] = None
    member_metadata: Optional[Any] = None
    secret: Optional[Any] = None
    flags: Optional[Any] = None

class create_lobby_params(msgspec.Struct):
    idle_timeout_seconds: Optional[Any] = None
    members: Optional[Any] = None
    metadata: Optional[Any] = None
    flags: Optional[Any] = None

class get_lobby_params(msgspec.Struct):
    lobby_id: Optional[Any] = None

class edit_lobby_params(msgspec.Struct):
    lobby_id: Optional[Any] = None
    idle_timeout_seconds: Optional[Any] = None
    metadata: Optional[Any] = None
    members: Optional[Any] = None
    flags: Optional[Any] = None

class edit_lobby_channel_link_params(msgspec.Struct):
    lobby_id: Optional[Any] = None
    channel_id: Optional[Any] = None

class leave_lobby_params(msgspec.Struct):
    lobby_id: Optional[Any] = None

class create_linked_lobby_guild_invite_for_self_params(msgspec.Struct):
    lobby_id: Optional[Any] = None

class bulk_update_lobby_members_params(msgspec.Struct):
    lobby_id: Optional[Any] = None

class add_lobby_member_params(msgspec.Struct):
    lobby_id: Optional[Any] = None
    user_id: Optional[Any] = None
    metadata: Optional[Any] = None
    flags: Optional[Any] = None

class delete_lobby_member_params(msgspec.Struct):
    lobby_id: Optional[Any] = None
    user_id: Optional[Any] = None

class create_linked_lobby_guild_invite_for_user_params(msgspec.Struct):
    lobby_id: Optional[Any] = None
    user_id: Optional[Any] = None

class get_lobby_messages_params(msgspec.Struct):
    lobby_id: Optional[Any] = None
    limit: Optional[int] = None

class create_lobby_message_params(msgspec.Struct):
    lobby_id: Optional[Any] = None
    content: Optional[Any] = None
    embeds: Optional[Any] = None
    allowed_mentions: Optional[Any] = None
    sticker_ids: Optional[Any] = None
    components: Optional[Any] = None
    flags: Optional[Any] = None
    attachments: Optional[Any] = None
    poll: Optional[Any] = None
    shared_client_theme: Optional[Any] = None
    confetti_potion: Optional[Any] = None
    message_reference: Optional[Any] = None
    nonce: Optional[Any] = None
    enforce_nonce: Optional[Any] = None
    tts: Optional[Any] = None

class get_my_oauth2_authorization_params(msgspec.Struct):
    pass

class get_my_oauth2_application_params(msgspec.Struct):
    pass

class get_public_keys_params(msgspec.Struct):
    pass

class get_openid_connect_userinfo_params(msgspec.Struct):
    pass

class partner_sdk_unmerge_provisional_account_params(msgspec.Struct):
    client_id: Optional[Any] = None
    client_secret: Optional[Any] = None
    external_auth_token: Optional[Any] = None
    external_auth_type: Optional[Any] = None

class partner_sdk_token_params(msgspec.Struct):
    client_id: Optional[Any] = None
    client_secret: Optional[Any] = None
    external_auth_token: Optional[Any] = None
    external_auth_type: Optional[Any] = None

class bot_partner_sdk_token_params(msgspec.Struct):
    external_user_id: Optional[Any] = None
    preferred_global_name: Optional[Any] = None

class get_soundboard_default_sounds_params(msgspec.Struct):
    pass

class create_stage_instance_params(msgspec.Struct):
    topic: Optional[Any] = None
    channel_id: Optional[Any] = None
    privacy_level: Optional[Any] = None
    guild_scheduled_event_id: Optional[Any] = None
    send_start_notification: Optional[Any] = None

class get_stage_instance_params(msgspec.Struct):
    channel_id: Optional[Any] = None

class delete_stage_instance_params(msgspec.Struct):
    channel_id: Optional[Any] = None

class update_stage_instance_params(msgspec.Struct):
    channel_id: Optional[Any] = None
    topic: Optional[Any] = None
    privacy_level: Optional[Any] = None

class list_sticker_packs_params(msgspec.Struct):
    pass

class get_sticker_pack_params(msgspec.Struct):
    pack_id: Optional[Any] = None

class get_sticker_params(msgspec.Struct):
    sticker_id: Optional[Any] = None

class get_my_user_params(msgspec.Struct):
    pass

class update_my_user_params(msgspec.Struct):
    username: Optional[Any] = None
    avatar: Optional[Any] = None
    banner: Optional[Any] = None

class get_application_user_role_connection_params(msgspec.Struct):
    application_id: Optional[Any] = None

class update_application_user_role_connection_params(msgspec.Struct):
    application_id: Optional[Any] = None
    platform_name: Optional[Any] = None
    platform_username: Optional[Any] = None
    metadata: Optional[Any] = None

class delete_application_user_role_connection_params(msgspec.Struct):
    application_id: Optional[Any] = None

class create_dm_params(msgspec.Struct):
    recipient_id: Optional[Any] = None
    access_tokens: Optional[Any] = None
    nicks: Optional[Any] = None

class list_my_connections_params(msgspec.Struct):
    pass

class list_my_guilds_params(msgspec.Struct):
    before: Optional[Any] = None
    after: Optional[Any] = None
    limit: Optional[int] = None
    with_counts: Optional[bool] = None

class leave_guild_params(msgspec.Struct):
    guild_id: Optional[Any] = None

class get_my_guild_member_params(msgspec.Struct):
    guild_id: Optional[Any] = None

class get_user_params(msgspec.Struct):
    user_id: Optional[Any] = None

class list_voice_regions_params(msgspec.Struct):
    pass

class get_webhook_params(msgspec.Struct):
    webhook_id: Optional[Any] = None

class delete_webhook_params(msgspec.Struct):
    webhook_id: Optional[Any] = None

class update_webhook_params(msgspec.Struct):
    webhook_id: Optional[Any] = None
    name: Optional[Any] = None
    avatar: Optional[Any] = None
    channel_id: Optional[Any] = None

class get_webhook_by_token_params(msgspec.Struct):
    webhook_id: Optional[Any] = None
    webhook_token: Optional[str] = None

class execute_webhook_params(msgspec.Struct):
    webhook_id: Optional[Any] = None
    webhook_token: Optional[str] = None
    wait: Optional[bool] = None
    thread_id: Optional[Any] = None
    with_components: Optional[bool] = None

class delete_webhook_by_token_params(msgspec.Struct):
    webhook_id: Optional[Any] = None
    webhook_token: Optional[str] = None

class update_webhook_by_token_params(msgspec.Struct):
    webhook_id: Optional[Any] = None
    webhook_token: Optional[str] = None
    name: Optional[Any] = None
    avatar: Optional[Any] = None

class execute_github_compatible_webhook_params(msgspec.Struct):
    webhook_id: Optional[Any] = None
    webhook_token: Optional[str] = None
    wait: Optional[bool] = None
    thread_id: Optional[Any] = None
    action: Optional[Any] = None
    ref: Optional[Any] = None
    ref_type: Optional[Any] = None
    comment: Optional[Any] = None
    issue: Optional[Any] = None
    pull_request: Optional[Any] = None
    repository: Optional[Any] = None
    forkee: Optional[Any] = None
    sender: Optional[Any] = None
    member: Optional[Any] = None
    release: Optional[Any] = None
    head_commit: Optional[Any] = None
    commits: Optional[Any] = None
    forced: Optional[Any] = None
    compare: Optional[Any] = None
    review: Optional[Any] = None
    check_run: Optional[Any] = None
    check_suite: Optional[Any] = None
    discussion: Optional[Any] = None
    answer: Optional[Any] = None

class get_original_webhook_message_params(msgspec.Struct):
    webhook_id: Optional[Any] = None
    webhook_token: Optional[str] = None
    thread_id: Optional[Any] = None

class delete_original_webhook_message_params(msgspec.Struct):
    webhook_id: Optional[Any] = None
    webhook_token: Optional[str] = None
    thread_id: Optional[Any] = None

class update_original_webhook_message_params(msgspec.Struct):
    webhook_id: Optional[Any] = None
    webhook_token: Optional[str] = None
    thread_id: Optional[Any] = None
    with_components: Optional[bool] = None
    content: Optional[Any] = None
    embeds: Optional[Any] = None
    allowed_mentions: Optional[Any] = None
    components: Optional[Any] = None
    attachments: Optional[Any] = None
    poll: Optional[Any] = None
    flags: Optional[Any] = None
    files_0: Optional[Any] = None
    files_1: Optional[Any] = None
    files_2: Optional[Any] = None
    files_3: Optional[Any] = None
    files_4: Optional[Any] = None
    files_5: Optional[Any] = None
    files_6: Optional[Any] = None
    files_7: Optional[Any] = None
    files_8: Optional[Any] = None
    files_9: Optional[Any] = None

class get_webhook_message_params(msgspec.Struct):
    webhook_id: Optional[Any] = None
    webhook_token: Optional[str] = None
    message_id: Optional[Any] = None
    thread_id: Optional[Any] = None

class delete_webhook_message_params(msgspec.Struct):
    webhook_id: Optional[Any] = None
    webhook_token: Optional[str] = None
    message_id: Optional[Any] = None
    thread_id: Optional[Any] = None

class update_webhook_message_params(msgspec.Struct):
    webhook_id: Optional[Any] = None
    webhook_token: Optional[str] = None
    message_id: Optional[Any] = None
    thread_id: Optional[Any] = None
    with_components: Optional[bool] = None
    content: Optional[Any] = None
    embeds: Optional[Any] = None
    allowed_mentions: Optional[Any] = None
    components: Optional[Any] = None
    attachments: Optional[Any] = None
    poll: Optional[Any] = None
    flags: Optional[Any] = None
    files_0: Optional[Any] = None
    files_1: Optional[Any] = None
    files_2: Optional[Any] = None
    files_3: Optional[Any] = None
    files_4: Optional[Any] = None
    files_5: Optional[Any] = None
    files_6: Optional[Any] = None
    files_7: Optional[Any] = None
    files_8: Optional[Any] = None
    files_9: Optional[Any] = None

class execute_slack_compatible_webhook_params(msgspec.Struct):
    webhook_id: Optional[Any] = None
    webhook_token: Optional[str] = None
    wait: Optional[bool] = None
    thread_id: Optional[Any] = None
    text: Optional[Any] = None
    username: Optional[Any] = None
    icon_url: Optional[Any] = None
    attachments: Optional[Any] = None
