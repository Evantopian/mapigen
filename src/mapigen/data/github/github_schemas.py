import msgspec
from typing import Optional, List, Any

class meta_root_params(msgspec.Struct):
    pass

class security_advisories_list_global_advisories_params(msgspec.Struct):
    ghsa_id: Optional[str] = None
    type: Optional[str] = None
    cve_id: Optional[str] = None
    ecosystem: Optional[Any] = None
    severity: Optional[str] = None
    cwes: Optional[Any] = None
    is_withdrawn: Optional[bool] = None
    affects: Optional[Any] = None
    published: Optional[str] = None
    updated: Optional[str] = None
    modified: Optional[str] = None
    epss_percentage: Optional[str] = None
    epss_percentile: Optional[str] = None
    before: Optional[str] = None
    after: Optional[str] = None
    direction: Optional[str] = None
    per_page: Optional[int] = None
    sort: Optional[str] = None

class security_advisories_get_global_advisory_params(msgspec.Struct):
    ghsa_id: Optional[str] = None

class apps_get_authenticated_params(msgspec.Struct):
    pass

class apps_create_from_manifest_params(msgspec.Struct):
    code: Optional[str] = None

class apps_get_webhook_config_for_app_params(msgspec.Struct):
    pass

class apps_update_webhook_config_for_app_params(msgspec.Struct):
    url: Optional[Any] = None
    content_type: Optional[Any] = None
    secret: Optional[Any] = None
    insecure_ssl: Optional[Any] = None

class apps_list_webhook_deliveries_params(msgspec.Struct):
    per_page: Optional[int] = None
    cursor: Optional[str] = None

class apps_get_webhook_delivery_params(msgspec.Struct):
    delivery_id: Optional[int] = None

class apps_redeliver_webhook_delivery_params(msgspec.Struct):
    delivery_id: Optional[int] = None

class apps_list_installation_requests_for_authenticated_app_params(msgspec.Struct):
    per_page: Optional[int] = None
    page: Optional[int] = None

class apps_list_installations_params(msgspec.Struct):
    per_page: Optional[int] = None
    page: Optional[int] = None
    since: Optional[str] = None
    outdated: Optional[str] = None

class apps_get_installation_params(msgspec.Struct):
    installation_id: Optional[int] = None

class apps_delete_installation_params(msgspec.Struct):
    installation_id: Optional[int] = None

class apps_create_installation_access_token_params(msgspec.Struct):
    installation_id: Optional[int] = None
    repositories: Optional[Any] = None
    repository_ids: Optional[Any] = None
    permissions: Optional[Any] = None

class apps_suspend_installation_params(msgspec.Struct):
    installation_id: Optional[int] = None

class apps_unsuspend_installation_params(msgspec.Struct):
    installation_id: Optional[int] = None

class apps_delete_authorization_params(msgspec.Struct):
    client_id: Optional[str] = None
    access_token: Optional[Any] = None

class apps_check_token_params(msgspec.Struct):
    client_id: Optional[str] = None
    access_token: Optional[Any] = None

class apps_reset_token_params(msgspec.Struct):
    client_id: Optional[str] = None
    access_token: Optional[Any] = None

class apps_delete_token_params(msgspec.Struct):
    client_id: Optional[str] = None
    access_token: Optional[Any] = None

class apps_scope_token_params(msgspec.Struct):
    client_id: Optional[str] = None
    access_token: Optional[Any] = None
    target: Optional[Any] = None
    target_id: Optional[Any] = None
    repositories: Optional[Any] = None
    repository_ids: Optional[Any] = None
    permissions: Optional[Any] = None

class apps_get_by_slug_params(msgspec.Struct):
    app_slug: Optional[str] = None

class classroom_get_an_assignment_params(msgspec.Struct):
    assignment_id: Optional[int] = None

class classroom_list_accepted_assignments_for_an_assignment_params(msgspec.Struct):
    assignment_id: Optional[int] = None
    page: Optional[int] = None
    per_page: Optional[int] = None

class classroom_get_assignment_grades_params(msgspec.Struct):
    assignment_id: Optional[int] = None

class classroom_list_classrooms_params(msgspec.Struct):
    page: Optional[int] = None
    per_page: Optional[int] = None

class classroom_get_a_classroom_params(msgspec.Struct):
    classroom_id: Optional[int] = None

class classroom_list_assignments_for_a_classroom_params(msgspec.Struct):
    classroom_id: Optional[int] = None
    page: Optional[int] = None
    per_page: Optional[int] = None

class codes_of_conduct_get_all_codes_of_conduct_params(msgspec.Struct):
    pass

class codes_of_conduct_get_conduct_code_params(msgspec.Struct):
    key: Optional[str] = None

class credentials_revoke_params(msgspec.Struct):
    credentials: Optional[Any] = None

class emojis_get_params(msgspec.Struct):
    pass

class code_security_get_configurations_for_enterprise_params(msgspec.Struct):
    enterprise: Optional[str] = None
    per_page: Optional[int] = None
    before: Optional[str] = None
    after: Optional[str] = None

class code_security_create_configuration_for_enterprise_params(msgspec.Struct):
    enterprise: Optional[str] = None
    name: Optional[Any] = None
    description: Optional[Any] = None
    advanced_security: Optional[Any] = None
    code_security: Optional[Any] = None
    dependency_graph: Optional[Any] = None
    dependency_graph_autosubmit_action: Optional[Any] = None
    dependency_graph_autosubmit_action_options: Optional[Any] = None
    dependabot_alerts: Optional[Any] = None
    dependabot_security_updates: Optional[Any] = None
    code_scanning_options: Optional[Any] = None
    code_scanning_default_setup: Optional[Any] = None
    code_scanning_default_setup_options: Optional[Any] = None
    code_scanning_delegated_alert_dismissal: Optional[Any] = None
    secret_protection: Optional[Any] = None
    secret_scanning: Optional[Any] = None
    secret_scanning_push_protection: Optional[Any] = None
    secret_scanning_validity_checks: Optional[Any] = None
    secret_scanning_non_provider_patterns: Optional[Any] = None
    secret_scanning_generic_secrets: Optional[Any] = None
    secret_scanning_delegated_alert_dismissal: Optional[Any] = None
    private_vulnerability_reporting: Optional[Any] = None
    enforcement: Optional[Any] = None

class code_security_get_default_configurations_for_enterprise_params(msgspec.Struct):
    enterprise: Optional[str] = None

class code_security_get_single_configuration_for_enterprise_params(msgspec.Struct):
    enterprise: Optional[str] = None
    configuration_id: Optional[int] = None

class code_security_update_enterprise_configuration_params(msgspec.Struct):
    enterprise: Optional[str] = None
    configuration_id: Optional[int] = None
    name: Optional[Any] = None
    description: Optional[Any] = None
    advanced_security: Optional[Any] = None
    code_security: Optional[Any] = None
    dependency_graph: Optional[Any] = None
    dependency_graph_autosubmit_action: Optional[Any] = None
    dependency_graph_autosubmit_action_options: Optional[Any] = None
    dependabot_alerts: Optional[Any] = None
    dependabot_security_updates: Optional[Any] = None
    code_scanning_default_setup: Optional[Any] = None
    code_scanning_default_setup_options: Optional[Any] = None
    code_scanning_delegated_alert_dismissal: Optional[Any] = None
    secret_protection: Optional[Any] = None
    secret_scanning: Optional[Any] = None
    secret_scanning_push_protection: Optional[Any] = None
    secret_scanning_validity_checks: Optional[Any] = None
    secret_scanning_non_provider_patterns: Optional[Any] = None
    secret_scanning_generic_secrets: Optional[Any] = None
    secret_scanning_delegated_alert_dismissal: Optional[Any] = None
    private_vulnerability_reporting: Optional[Any] = None
    enforcement: Optional[Any] = None

class code_security_delete_configuration_for_enterprise_params(msgspec.Struct):
    enterprise: Optional[str] = None
    configuration_id: Optional[int] = None

class code_security_attach_enterprise_configuration_params(msgspec.Struct):
    enterprise: Optional[str] = None
    configuration_id: Optional[int] = None
    scope: Optional[Any] = None

class code_security_set_configuration_as_default_for_enterprise_params(msgspec.Struct):
    enterprise: Optional[str] = None
    configuration_id: Optional[int] = None
    default_for_new_repos: Optional[Any] = None

class code_security_get_repositories_for_enterprise_configuration_params(msgspec.Struct):
    enterprise: Optional[str] = None
    configuration_id: Optional[int] = None
    per_page: Optional[int] = None
    before: Optional[str] = None
    after: Optional[str] = None
    status: Optional[str] = None

class dependabot_list_alerts_for_enterprise_params(msgspec.Struct):
    enterprise: Optional[str] = None
    state: Optional[str] = None
    severity: Optional[str] = None
    ecosystem: Optional[str] = None
    package: Optional[str] = None
    epss_percentage: Optional[str] = None
    has: Optional[Any] = None
    scope: Optional[str] = None
    sort: Optional[str] = None
    direction: Optional[str] = None
    before: Optional[str] = None
    after: Optional[str] = None
    first: Optional[int] = None
    last: Optional[int] = None
    per_page: Optional[int] = None

class secret_scanning_list_alerts_for_enterprise_params(msgspec.Struct):
    enterprise: Optional[str] = None
    state: Optional[str] = None
    secret_type: Optional[str] = None
    resolution: Optional[str] = None
    sort: Optional[str] = None
    direction: Optional[str] = None
    per_page: Optional[int] = None
    before: Optional[str] = None
    after: Optional[str] = None
    validity: Optional[str] = None
    is_publicly_leaked: Optional[bool] = None
    is_multi_repo: Optional[bool] = None
    hide_secret: Optional[bool] = None

class activity_list_public_events_params(msgspec.Struct):
    per_page: Optional[int] = None
    page: Optional[int] = None

class activity_get_feeds_params(msgspec.Struct):
    pass

class gists_list_params(msgspec.Struct):
    since: Optional[str] = None
    per_page: Optional[int] = None
    page: Optional[int] = None

class gists_create_params(msgspec.Struct):
    description: Optional[Any] = None
    files: Optional[Any] = None
    public: Optional[Any] = None

class gists_list_public_params(msgspec.Struct):
    since: Optional[str] = None
    per_page: Optional[int] = None
    page: Optional[int] = None

class gists_list_starred_params(msgspec.Struct):
    since: Optional[str] = None
    per_page: Optional[int] = None
    page: Optional[int] = None

class gists_get_params(msgspec.Struct):
    gist_id: Optional[str] = None

class gists_update_params(msgspec.Struct):
    gist_id: Optional[str] = None
    description: Optional[Any] = None
    files: Optional[Any] = None

class gists_delete_params(msgspec.Struct):
    gist_id: Optional[str] = None

class gists_list_comments_params(msgspec.Struct):
    gist_id: Optional[str] = None
    per_page: Optional[int] = None
    page: Optional[int] = None

class gists_create_comment_params(msgspec.Struct):
    gist_id: Optional[str] = None
    body: Optional[Any] = None

class gists_get_comment_params(msgspec.Struct):
    gist_id: Optional[str] = None
    comment_id: Optional[int] = None

class gists_update_comment_params(msgspec.Struct):
    gist_id: Optional[str] = None
    comment_id: Optional[int] = None
    body: Optional[Any] = None

class gists_delete_comment_params(msgspec.Struct):
    gist_id: Optional[str] = None
    comment_id: Optional[int] = None

class gists_list_commits_params(msgspec.Struct):
    gist_id: Optional[str] = None
    per_page: Optional[int] = None
    page: Optional[int] = None

class gists_list_forks_params(msgspec.Struct):
    gist_id: Optional[str] = None
    per_page: Optional[int] = None
    page: Optional[int] = None

class gists_fork_params(msgspec.Struct):
    gist_id: Optional[str] = None

class gists_check_is_starred_params(msgspec.Struct):
    gist_id: Optional[str] = None

class gists_star_params(msgspec.Struct):
    gist_id: Optional[str] = None

class gists_unstar_params(msgspec.Struct):
    gist_id: Optional[str] = None

class gists_get_revision_params(msgspec.Struct):
    gist_id: Optional[str] = None
    sha: Optional[str] = None

class gitignore_get_all_templates_params(msgspec.Struct):
    pass

class gitignore_get_template_params(msgspec.Struct):
    name: Optional[str] = None

class apps_list_repos_accessible_to_installation_params(msgspec.Struct):
    per_page: Optional[int] = None
    page: Optional[int] = None

class apps_revoke_installation_access_token_params(msgspec.Struct):
    pass

class issues_list_params(msgspec.Struct):
    filter: Optional[str] = None
    state: Optional[str] = None
    labels: Optional[str] = None
    sort: Optional[str] = None
    direction: Optional[str] = None
    since: Optional[str] = None
    collab: Optional[bool] = None
    orgs: Optional[bool] = None
    owned: Optional[bool] = None
    pulls: Optional[bool] = None
    per_page: Optional[int] = None
    page: Optional[int] = None

class licenses_get_all_commonly_used_params(msgspec.Struct):
    featured: Optional[bool] = None
    per_page: Optional[int] = None
    page: Optional[int] = None

class licenses_get_params(msgspec.Struct):
    license: Optional[str] = None

class markdown_render_params(msgspec.Struct):
    text: Optional[Any] = None
    mode: Optional[Any] = None
    context: Optional[Any] = None

class markdown_render_raw_params(msgspec.Struct):
    pass

class apps_get_subscription_plan_for_account_params(msgspec.Struct):
    account_id: Optional[int] = None

class apps_list_plans_params(msgspec.Struct):
    per_page: Optional[int] = None
    page: Optional[int] = None

class apps_list_accounts_for_plan_params(msgspec.Struct):
    plan_id: Optional[int] = None
    sort: Optional[str] = None
    direction: Optional[str] = None
    per_page: Optional[int] = None
    page: Optional[int] = None

class apps_get_subscription_plan_for_account_stubbed_params(msgspec.Struct):
    account_id: Optional[int] = None

class apps_list_plans_stubbed_params(msgspec.Struct):
    per_page: Optional[int] = None
    page: Optional[int] = None

class apps_list_accounts_for_plan_stubbed_params(msgspec.Struct):
    plan_id: Optional[int] = None
    sort: Optional[str] = None
    direction: Optional[str] = None
    per_page: Optional[int] = None
    page: Optional[int] = None

class meta_get_params(msgspec.Struct):
    pass

class activity_list_public_events_for_repo_network_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    per_page: Optional[int] = None
    page: Optional[int] = None

class activity_list_notifications_for_authenticated_user_params(msgspec.Struct):
    all: Optional[bool] = None
    participating: Optional[bool] = None
    since: Optional[str] = None
    before: Optional[str] = None
    page: Optional[int] = None
    per_page: Optional[int] = None

class activity_mark_notifications_as_read_params(msgspec.Struct):
    last_read_at: Optional[Any] = None
    read: Optional[Any] = None

class activity_get_thread_params(msgspec.Struct):
    thread_id: Optional[int] = None

class activity_mark_thread_as_read_params(msgspec.Struct):
    thread_id: Optional[int] = None

class activity_mark_thread_as_done_params(msgspec.Struct):
    thread_id: Optional[int] = None

class activity_get_thread_subscription_for_authenticated_user_params(msgspec.Struct):
    thread_id: Optional[int] = None

class activity_set_thread_subscription_params(msgspec.Struct):
    thread_id: Optional[int] = None
    ignored: Optional[Any] = None

class activity_delete_thread_subscription_params(msgspec.Struct):
    thread_id: Optional[int] = None

class meta_get_octocat_params(msgspec.Struct):
    s: Optional[str] = None

class orgs_list_params(msgspec.Struct):
    since: Optional[int] = None
    per_page: Optional[int] = None

class dependabot_repository_access_for_org_params(msgspec.Struct):
    org: Optional[str] = None
    page: Optional[int] = None
    per_page: Optional[int] = None

class dependabot_update_repository_access_for_org_params(msgspec.Struct):
    org: Optional[str] = None
    repository_ids_to_add: Optional[Any] = None
    repository_ids_to_remove: Optional[Any] = None

class dependabot_set_repository_access_default_level_params(msgspec.Struct):
    org: Optional[str] = None
    default_level: Optional[Any] = None

class billing_get_github_billing_usage_report_org_params(msgspec.Struct):
    org: Optional[str] = None
    year: Optional[int] = None
    month: Optional[int] = None
    day: Optional[int] = None
    hour: Optional[int] = None

class orgs_get_params(msgspec.Struct):
    org: Optional[str] = None

class orgs_update_params(msgspec.Struct):
    org: Optional[str] = None
    billing_email: Optional[Any] = None
    company: Optional[Any] = None
    email: Optional[Any] = None
    twitter_username: Optional[Any] = None
    location: Optional[Any] = None
    name: Optional[Any] = None
    description: Optional[Any] = None
    has_organization_projects: Optional[Any] = None
    has_repository_projects: Optional[Any] = None
    default_repository_permission: Optional[Any] = None
    members_can_create_repositories: Optional[Any] = None
    members_can_create_internal_repositories: Optional[Any] = None
    members_can_create_private_repositories: Optional[Any] = None
    members_can_create_public_repositories: Optional[Any] = None
    members_allowed_repository_creation_type: Optional[Any] = None
    members_can_create_pages: Optional[Any] = None
    members_can_create_public_pages: Optional[Any] = None
    members_can_create_private_pages: Optional[Any] = None
    members_can_fork_private_repositories: Optional[Any] = None
    web_commit_signoff_required: Optional[Any] = None
    blog: Optional[Any] = None
    advanced_security_enabled_for_new_repositories: Optional[Any] = None
    dependabot_alerts_enabled_for_new_repositories: Optional[Any] = None
    dependabot_security_updates_enabled_for_new_repositories: Optional[Any] = None
    dependency_graph_enabled_for_new_repositories: Optional[Any] = None
    secret_scanning_enabled_for_new_repositories: Optional[Any] = None
    secret_scanning_push_protection_enabled_for_new_repositories: Optional[Any] = None
    secret_scanning_push_protection_custom_link_enabled: Optional[Any] = None
    secret_scanning_push_protection_custom_link: Optional[Any] = None
    deploy_keys_enabled_for_repositories: Optional[Any] = None

class orgs_delete_params(msgspec.Struct):
    org: Optional[str] = None

class actions_get_actions_cache_usage_for_org_params(msgspec.Struct):
    org: Optional[str] = None

class actions_get_actions_cache_usage_by_repo_for_org_params(msgspec.Struct):
    org: Optional[str] = None
    per_page: Optional[int] = None
    page: Optional[int] = None

class actions_list_hosted_runners_for_org_params(msgspec.Struct):
    org: Optional[str] = None
    per_page: Optional[int] = None
    page: Optional[int] = None

class actions_create_hosted_runner_for_org_params(msgspec.Struct):
    org: Optional[str] = None
    name: Optional[Any] = None
    image: Optional[Any] = None
    size: Optional[Any] = None
    runner_group_id: Optional[Any] = None
    maximum_runners: Optional[Any] = None
    enable_static_ip: Optional[Any] = None

class actions_get_hosted_runners_github_owned_images_for_org_params(msgspec.Struct):
    org: Optional[str] = None

class actions_get_hosted_runners_partner_images_for_org_params(msgspec.Struct):
    org: Optional[str] = None

class actions_get_hosted_runners_limits_for_org_params(msgspec.Struct):
    org: Optional[str] = None

class actions_get_hosted_runners_machine_specs_for_org_params(msgspec.Struct):
    org: Optional[str] = None

class actions_get_hosted_runners_platforms_for_org_params(msgspec.Struct):
    org: Optional[str] = None

class actions_get_hosted_runner_for_org_params(msgspec.Struct):
    org: Optional[str] = None
    hosted_runner_id: Optional[int] = None

class actions_update_hosted_runner_for_org_params(msgspec.Struct):
    org: Optional[str] = None
    hosted_runner_id: Optional[int] = None
    name: Optional[Any] = None
    runner_group_id: Optional[Any] = None
    maximum_runners: Optional[Any] = None
    enable_static_ip: Optional[Any] = None

class actions_delete_hosted_runner_for_org_params(msgspec.Struct):
    org: Optional[str] = None
    hosted_runner_id: Optional[int] = None

class oidc_get_oidc_custom_sub_template_for_org_params(msgspec.Struct):
    org: Optional[str] = None

class oidc_update_oidc_custom_sub_template_for_org_params(msgspec.Struct):
    org: Optional[str] = None
    include_claim_keys: Optional[Any] = None

class actions_get_github_actions_permissions_organization_params(msgspec.Struct):
    org: Optional[str] = None

class actions_set_github_actions_permissions_organization_params(msgspec.Struct):
    org: Optional[str] = None
    enabled_repositories: Optional[Any] = None
    allowed_actions: Optional[Any] = None
    sha_pinning_required: Optional[Any] = None

class actions_get_artifact_and_log_retention_settings_organization_params(msgspec.Struct):
    org: Optional[str] = None

class actions_set_artifact_and_log_retention_settings_organization_params(msgspec.Struct):
    org: Optional[str] = None
    days: Optional[Any] = None

class actions_get_fork_pr_contributor_approval_permissions_organization_params(msgspec.Struct):
    org: Optional[str] = None

class actions_set_fork_pr_contributor_approval_permissions_organization_params(msgspec.Struct):
    org: Optional[str] = None
    approval_policy: Optional[Any] = None

class actions_get_private_repo_fork_pr_workflows_settings_organization_params(msgspec.Struct):
    org: Optional[str] = None

class actions_set_private_repo_fork_pr_workflows_settings_organization_params(msgspec.Struct):
    org: Optional[str] = None
    run_workflows_from_fork_pull_requests: Optional[Any] = None
    send_write_tokens_to_workflows: Optional[Any] = None
    send_secrets_and_variables: Optional[Any] = None
    require_approval_for_fork_pr_workflows: Optional[Any] = None

class actions_list_selected_repositories_enabled_github_actions_organization_params(msgspec.Struct):
    org: Optional[str] = None
    per_page: Optional[int] = None
    page: Optional[int] = None

class actions_set_selected_repositories_enabled_github_actions_organization_params(msgspec.Struct):
    org: Optional[str] = None
    selected_repository_ids: Optional[Any] = None

class actions_enable_selected_repository_github_actions_organization_params(msgspec.Struct):
    org: Optional[str] = None
    repository_id: Optional[int] = None

class actions_disable_selected_repository_github_actions_organization_params(msgspec.Struct):
    org: Optional[str] = None
    repository_id: Optional[int] = None

class actions_get_allowed_actions_organization_params(msgspec.Struct):
    org: Optional[str] = None

class actions_set_allowed_actions_organization_params(msgspec.Struct):
    org: Optional[str] = None
    github_owned_allowed: Optional[Any] = None
    verified_allowed: Optional[Any] = None
    patterns_allowed: Optional[Any] = None

class actions_get_self_hosted_runners_permissions_organization_params(msgspec.Struct):
    org: Optional[str] = None

class actions_set_self_hosted_runners_permissions_organization_params(msgspec.Struct):
    org: Optional[str] = None
    enabled_repositories: Optional[Any] = None

class actions_list_selected_repositories_self_hosted_runners_organization_params(msgspec.Struct):
    org: Optional[str] = None
    per_page: Optional[int] = None
    page: Optional[int] = None

class actions_set_selected_repositories_self_hosted_runners_organization_params(msgspec.Struct):
    org: Optional[str] = None
    selected_repository_ids: Optional[Any] = None

class actions_enable_selected_repository_self_hosted_runners_organization_params(msgspec.Struct):
    org: Optional[str] = None
    repository_id: Optional[int] = None

class actions_disable_selected_repository_self_hosted_runners_organization_params(msgspec.Struct):
    org: Optional[str] = None
    repository_id: Optional[int] = None

class actions_get_github_actions_default_workflow_permissions_organization_params(msgspec.Struct):
    org: Optional[str] = None

class actions_set_github_actions_default_workflow_permissions_organization_params(msgspec.Struct):
    org: Optional[str] = None
    default_workflow_permissions: Optional[Any] = None
    can_approve_pull_request_reviews: Optional[Any] = None

class actions_list_self_hosted_runner_groups_for_org_params(msgspec.Struct):
    org: Optional[str] = None
    per_page: Optional[int] = None
    page: Optional[int] = None
    visible_to_repository: Optional[str] = None

class actions_create_self_hosted_runner_group_for_org_params(msgspec.Struct):
    org: Optional[str] = None
    name: Optional[Any] = None
    visibility: Optional[Any] = None
    selected_repository_ids: Optional[Any] = None
    runners: Optional[Any] = None
    allows_public_repositories: Optional[Any] = None
    restricted_to_workflows: Optional[Any] = None
    selected_workflows: Optional[Any] = None
    network_configuration_id: Optional[Any] = None

class actions_get_self_hosted_runner_group_for_org_params(msgspec.Struct):
    org: Optional[str] = None
    runner_group_id: Optional[int] = None

class actions_update_self_hosted_runner_group_for_org_params(msgspec.Struct):
    org: Optional[str] = None
    runner_group_id: Optional[int] = None
    name: Optional[Any] = None
    visibility: Optional[Any] = None
    allows_public_repositories: Optional[Any] = None
    restricted_to_workflows: Optional[Any] = None
    selected_workflows: Optional[Any] = None
    network_configuration_id: Optional[Any] = None

class actions_delete_self_hosted_runner_group_from_org_params(msgspec.Struct):
    org: Optional[str] = None
    runner_group_id: Optional[int] = None

class actions_list_github_hosted_runners_in_group_for_org_params(msgspec.Struct):
    org: Optional[str] = None
    runner_group_id: Optional[int] = None
    per_page: Optional[int] = None
    page: Optional[int] = None

class actions_list_repo_access_to_self_hosted_runner_group_in_org_params(msgspec.Struct):
    org: Optional[str] = None
    runner_group_id: Optional[int] = None
    page: Optional[int] = None
    per_page: Optional[int] = None

class actions_set_repo_access_to_self_hosted_runner_group_in_org_params(msgspec.Struct):
    org: Optional[str] = None
    runner_group_id: Optional[int] = None
    selected_repository_ids: Optional[Any] = None

class actions_add_repo_access_to_self_hosted_runner_group_in_org_params(msgspec.Struct):
    org: Optional[str] = None
    runner_group_id: Optional[int] = None
    repository_id: Optional[int] = None

class actions_remove_repo_access_to_self_hosted_runner_group_in_org_params(msgspec.Struct):
    org: Optional[str] = None
    runner_group_id: Optional[int] = None
    repository_id: Optional[int] = None

class actions_list_self_hosted_runners_in_group_for_org_params(msgspec.Struct):
    org: Optional[str] = None
    runner_group_id: Optional[int] = None
    per_page: Optional[int] = None
    page: Optional[int] = None

class actions_set_self_hosted_runners_in_group_for_org_params(msgspec.Struct):
    org: Optional[str] = None
    runner_group_id: Optional[int] = None
    runners: Optional[Any] = None

class actions_add_self_hosted_runner_to_group_for_org_params(msgspec.Struct):
    org: Optional[str] = None
    runner_group_id: Optional[int] = None
    runner_id: Optional[int] = None

class actions_remove_self_hosted_runner_from_group_for_org_params(msgspec.Struct):
    org: Optional[str] = None
    runner_group_id: Optional[int] = None
    runner_id: Optional[int] = None

class actions_list_self_hosted_runners_for_org_params(msgspec.Struct):
    name: Optional[str] = None
    org: Optional[str] = None
    per_page: Optional[int] = None
    page: Optional[int] = None

class actions_list_runner_applications_for_org_params(msgspec.Struct):
    org: Optional[str] = None

class actions_generate_runner_jitconfig_for_org_params(msgspec.Struct):
    org: Optional[str] = None
    name: Optional[Any] = None
    runner_group_id: Optional[Any] = None
    labels: Optional[Any] = None
    work_folder: Optional[Any] = None

class actions_create_registration_token_for_org_params(msgspec.Struct):
    org: Optional[str] = None

class actions_create_remove_token_for_org_params(msgspec.Struct):
    org: Optional[str] = None

class actions_get_self_hosted_runner_for_org_params(msgspec.Struct):
    org: Optional[str] = None
    runner_id: Optional[int] = None

class actions_delete_self_hosted_runner_from_org_params(msgspec.Struct):
    org: Optional[str] = None
    runner_id: Optional[int] = None

class actions_list_labels_for_self_hosted_runner_for_org_params(msgspec.Struct):
    org: Optional[str] = None
    runner_id: Optional[int] = None

class actions_add_custom_labels_to_self_hosted_runner_for_org_params(msgspec.Struct):
    org: Optional[str] = None
    runner_id: Optional[int] = None
    labels: Optional[Any] = None

class actions_set_custom_labels_for_self_hosted_runner_for_org_params(msgspec.Struct):
    org: Optional[str] = None
    runner_id: Optional[int] = None
    labels: Optional[Any] = None

class actions_remove_all_custom_labels_from_self_hosted_runner_for_org_params(msgspec.Struct):
    org: Optional[str] = None
    runner_id: Optional[int] = None

class actions_remove_custom_label_from_self_hosted_runner_for_org_params(msgspec.Struct):
    org: Optional[str] = None
    runner_id: Optional[int] = None
    name: Optional[str] = None

class actions_list_org_secrets_params(msgspec.Struct):
    org: Optional[str] = None
    per_page: Optional[int] = None
    page: Optional[int] = None

class actions_get_org_public_key_params(msgspec.Struct):
    org: Optional[str] = None

class actions_get_org_secret_params(msgspec.Struct):
    org: Optional[str] = None
    secret_name: Optional[str] = None

class actions_create_or_update_org_secret_params(msgspec.Struct):
    org: Optional[str] = None
    secret_name: Optional[str] = None
    encrypted_value: Optional[Any] = None
    key_id: Optional[Any] = None
    visibility: Optional[Any] = None
    selected_repository_ids: Optional[Any] = None

class actions_delete_org_secret_params(msgspec.Struct):
    org: Optional[str] = None
    secret_name: Optional[str] = None

class actions_list_selected_repos_for_org_secret_params(msgspec.Struct):
    org: Optional[str] = None
    secret_name: Optional[str] = None
    page: Optional[int] = None
    per_page: Optional[int] = None

class actions_set_selected_repos_for_org_secret_params(msgspec.Struct):
    org: Optional[str] = None
    secret_name: Optional[str] = None
    selected_repository_ids: Optional[Any] = None

class actions_add_selected_repo_to_org_secret_params(msgspec.Struct):
    org: Optional[str] = None
    secret_name: Optional[str] = None
    repository_id: Optional[int] = None

class actions_remove_selected_repo_from_org_secret_params(msgspec.Struct):
    org: Optional[str] = None
    secret_name: Optional[str] = None
    repository_id: Optional[int] = None

class actions_list_org_variables_params(msgspec.Struct):
    org: Optional[str] = None
    per_page: Optional[int] = None
    page: Optional[int] = None

class actions_create_org_variable_params(msgspec.Struct):
    org: Optional[str] = None
    name: Optional[Any] = None
    value: Optional[Any] = None
    visibility: Optional[Any] = None
    selected_repository_ids: Optional[Any] = None

class actions_get_org_variable_params(msgspec.Struct):
    org: Optional[str] = None
    name: Optional[str] = None

class actions_update_org_variable_params(msgspec.Struct):
    org: Optional[str] = None
    name: Optional[str] = None
    name_: Optional[Any] = None
    value: Optional[Any] = None
    visibility: Optional[Any] = None
    selected_repository_ids: Optional[Any] = None

class actions_delete_org_variable_params(msgspec.Struct):
    org: Optional[str] = None
    name: Optional[str] = None

class actions_list_selected_repos_for_org_variable_params(msgspec.Struct):
    org: Optional[str] = None
    name: Optional[str] = None
    page: Optional[int] = None
    per_page: Optional[int] = None

class actions_set_selected_repos_for_org_variable_params(msgspec.Struct):
    org: Optional[str] = None
    name: Optional[str] = None
    selected_repository_ids: Optional[Any] = None

class actions_add_selected_repo_to_org_variable_params(msgspec.Struct):
    org: Optional[str] = None
    name: Optional[str] = None
    repository_id: Optional[int] = None

class actions_remove_selected_repo_from_org_variable_params(msgspec.Struct):
    org: Optional[str] = None
    name: Optional[str] = None
    repository_id: Optional[int] = None

class orgs_list_attestations_bulk_params(msgspec.Struct):
    per_page: Optional[int] = None
    before: Optional[str] = None
    after: Optional[str] = None
    org: Optional[str] = None
    subject_digests: Optional[Any] = None
    predicate_type: Optional[Any] = None

class orgs_delete_attestations_bulk_params(msgspec.Struct):
    org: Optional[str] = None

class orgs_delete_attestations_by_subject_digest_params(msgspec.Struct):
    org: Optional[str] = None
    subject_digest: Optional[str] = None

class orgs_delete_attestations_by_id_params(msgspec.Struct):
    org: Optional[str] = None
    attestation_id: Optional[int] = None

class orgs_list_attestations_params(msgspec.Struct):
    per_page: Optional[int] = None
    before: Optional[str] = None
    after: Optional[str] = None
    org: Optional[str] = None
    subject_digest: Optional[str] = None
    predicate_type: Optional[str] = None

class orgs_list_blocked_users_params(msgspec.Struct):
    org: Optional[str] = None
    per_page: Optional[int] = None
    page: Optional[int] = None

class orgs_check_blocked_user_params(msgspec.Struct):
    org: Optional[str] = None
    username: Optional[str] = None

class orgs_block_user_params(msgspec.Struct):
    org: Optional[str] = None
    username: Optional[str] = None

class orgs_unblock_user_params(msgspec.Struct):
    org: Optional[str] = None
    username: Optional[str] = None

class campaigns_list_org_campaigns_params(msgspec.Struct):
    org: Optional[str] = None
    page: Optional[int] = None
    per_page: Optional[int] = None
    direction: Optional[str] = None
    state: Optional[Any] = None
    sort: Optional[str] = None

class campaigns_create_campaign_params(msgspec.Struct):
    org: Optional[str] = None
    name: Optional[Any] = None
    description: Optional[Any] = None
    managers: Optional[Any] = None
    team_managers: Optional[Any] = None
    ends_at: Optional[Any] = None
    contact_link: Optional[Any] = None
    code_scanning_alerts: Optional[Any] = None
    generate_issues: Optional[Any] = None

class campaigns_get_campaign_summary_params(msgspec.Struct):
    org: Optional[str] = None
    campaign_number: Optional[int] = None

class campaigns_update_campaign_params(msgspec.Struct):
    org: Optional[str] = None
    campaign_number: Optional[int] = None
    name: Optional[Any] = None
    description: Optional[Any] = None
    managers: Optional[Any] = None
    team_managers: Optional[Any] = None
    ends_at: Optional[Any] = None
    contact_link: Optional[Any] = None
    state: Optional[Any] = None

class campaigns_delete_campaign_params(msgspec.Struct):
    org: Optional[str] = None
    campaign_number: Optional[int] = None

class code_scanning_list_alerts_for_org_params(msgspec.Struct):
    org: Optional[str] = None
    tool_name: Optional[Any] = None
    tool_guid: Optional[Any] = None
    before: Optional[str] = None
    after: Optional[str] = None
    page: Optional[int] = None
    per_page: Optional[int] = None
    direction: Optional[str] = None
    state: Optional[Any] = None
    sort: Optional[str] = None
    severity: Optional[Any] = None

class code_security_get_configurations_for_org_params(msgspec.Struct):
    org: Optional[str] = None
    target_type: Optional[str] = None
    per_page: Optional[int] = None
    before: Optional[str] = None
    after: Optional[str] = None

class code_security_create_configuration_params(msgspec.Struct):
    org: Optional[str] = None
    name: Optional[Any] = None
    description: Optional[Any] = None
    advanced_security: Optional[Any] = None
    code_security: Optional[Any] = None
    dependency_graph: Optional[Any] = None
    dependency_graph_autosubmit_action: Optional[Any] = None
    dependency_graph_autosubmit_action_options: Optional[Any] = None
    dependabot_alerts: Optional[Any] = None
    dependabot_security_updates: Optional[Any] = None
    code_scanning_options: Optional[Any] = None
    code_scanning_default_setup: Optional[Any] = None
    code_scanning_default_setup_options: Optional[Any] = None
    code_scanning_delegated_alert_dismissal: Optional[Any] = None
    secret_protection: Optional[Any] = None
    secret_scanning: Optional[Any] = None
    secret_scanning_push_protection: Optional[Any] = None
    secret_scanning_delegated_bypass: Optional[Any] = None
    secret_scanning_delegated_bypass_options: Optional[Any] = None
    secret_scanning_validity_checks: Optional[Any] = None
    secret_scanning_non_provider_patterns: Optional[Any] = None
    secret_scanning_generic_secrets: Optional[Any] = None
    secret_scanning_delegated_alert_dismissal: Optional[Any] = None
    private_vulnerability_reporting: Optional[Any] = None
    enforcement: Optional[Any] = None

class code_security_get_default_configurations_params(msgspec.Struct):
    org: Optional[str] = None

class code_security_detach_configuration_params(msgspec.Struct):
    org: Optional[str] = None
    selected_repository_ids: Optional[Any] = None

class code_security_get_configuration_params(msgspec.Struct):
    org: Optional[str] = None
    configuration_id: Optional[int] = None

class code_security_update_configuration_params(msgspec.Struct):
    org: Optional[str] = None
    configuration_id: Optional[int] = None
    name: Optional[Any] = None
    description: Optional[Any] = None
    advanced_security: Optional[Any] = None
    code_security: Optional[Any] = None
    dependency_graph: Optional[Any] = None
    dependency_graph_autosubmit_action: Optional[Any] = None
    dependency_graph_autosubmit_action_options: Optional[Any] = None
    dependabot_alerts: Optional[Any] = None
    dependabot_security_updates: Optional[Any] = None
    code_scanning_default_setup: Optional[Any] = None
    code_scanning_default_setup_options: Optional[Any] = None
    code_scanning_delegated_alert_dismissal: Optional[Any] = None
    secret_protection: Optional[Any] = None
    secret_scanning: Optional[Any] = None
    secret_scanning_push_protection: Optional[Any] = None
    secret_scanning_delegated_bypass: Optional[Any] = None
    secret_scanning_delegated_bypass_options: Optional[Any] = None
    secret_scanning_validity_checks: Optional[Any] = None
    secret_scanning_non_provider_patterns: Optional[Any] = None
    secret_scanning_generic_secrets: Optional[Any] = None
    secret_scanning_delegated_alert_dismissal: Optional[Any] = None
    private_vulnerability_reporting: Optional[Any] = None
    enforcement: Optional[Any] = None

class code_security_delete_configuration_params(msgspec.Struct):
    org: Optional[str] = None
    configuration_id: Optional[int] = None

class code_security_attach_configuration_params(msgspec.Struct):
    org: Optional[str] = None
    configuration_id: Optional[int] = None
    scope: Optional[Any] = None
    selected_repository_ids: Optional[Any] = None

class code_security_set_configuration_as_default_params(msgspec.Struct):
    org: Optional[str] = None
    configuration_id: Optional[int] = None
    default_for_new_repos: Optional[Any] = None

class code_security_get_repositories_for_configuration_params(msgspec.Struct):
    org: Optional[str] = None
    configuration_id: Optional[int] = None
    per_page: Optional[int] = None
    before: Optional[str] = None
    after: Optional[str] = None
    status: Optional[str] = None

class codespaces_list_in_organization_params(msgspec.Struct):
    per_page: Optional[int] = None
    page: Optional[int] = None
    org: Optional[str] = None

class codespaces_set_codespaces_access_params(msgspec.Struct):
    org: Optional[str] = None
    visibility: Optional[Any] = None
    selected_usernames: Optional[Any] = None

class codespaces_set_codespaces_access_users_params(msgspec.Struct):
    org: Optional[str] = None
    selected_usernames: Optional[Any] = None

class codespaces_delete_codespaces_access_users_params(msgspec.Struct):
    org: Optional[str] = None
    selected_usernames: Optional[Any] = None

class codespaces_list_org_secrets_params(msgspec.Struct):
    org: Optional[str] = None
    per_page: Optional[int] = None
    page: Optional[int] = None

class codespaces_get_org_public_key_params(msgspec.Struct):
    org: Optional[str] = None

class codespaces_get_org_secret_params(msgspec.Struct):
    org: Optional[str] = None
    secret_name: Optional[str] = None

class codespaces_create_or_update_org_secret_params(msgspec.Struct):
    org: Optional[str] = None
    secret_name: Optional[str] = None
    encrypted_value: Optional[Any] = None
    key_id: Optional[Any] = None
    visibility: Optional[Any] = None
    selected_repository_ids: Optional[Any] = None

class codespaces_delete_org_secret_params(msgspec.Struct):
    org: Optional[str] = None
    secret_name: Optional[str] = None

class codespaces_list_selected_repos_for_org_secret_params(msgspec.Struct):
    org: Optional[str] = None
    secret_name: Optional[str] = None
    page: Optional[int] = None
    per_page: Optional[int] = None

class codespaces_set_selected_repos_for_org_secret_params(msgspec.Struct):
    org: Optional[str] = None
    secret_name: Optional[str] = None
    selected_repository_ids: Optional[Any] = None

class codespaces_add_selected_repo_to_org_secret_params(msgspec.Struct):
    org: Optional[str] = None
    secret_name: Optional[str] = None
    repository_id: Optional[int] = None

class codespaces_remove_selected_repo_from_org_secret_params(msgspec.Struct):
    org: Optional[str] = None
    secret_name: Optional[str] = None
    repository_id: Optional[int] = None

class copilot_get_copilot_organization_details_params(msgspec.Struct):
    org: Optional[str] = None

class copilot_list_copilot_seats_params(msgspec.Struct):
    org: Optional[str] = None
    page: Optional[int] = None
    per_page: Optional[int] = None

class copilot_add_copilot_seats_for_teams_params(msgspec.Struct):
    org: Optional[str] = None
    selected_teams: Optional[Any] = None

class copilot_cancel_copilot_seat_assignment_for_teams_params(msgspec.Struct):
    org: Optional[str] = None
    selected_teams: Optional[Any] = None

class copilot_add_copilot_seats_for_users_params(msgspec.Struct):
    org: Optional[str] = None
    selected_usernames: Optional[Any] = None

class copilot_cancel_copilot_seat_assignment_for_users_params(msgspec.Struct):
    org: Optional[str] = None
    selected_usernames: Optional[Any] = None

class copilot_copilot_metrics_for_organization_params(msgspec.Struct):
    org: Optional[str] = None
    since: Optional[str] = None
    until: Optional[str] = None
    page: Optional[int] = None
    per_page: Optional[int] = None

class dependabot_list_alerts_for_org_params(msgspec.Struct):
    org: Optional[str] = None
    state: Optional[str] = None
    severity: Optional[str] = None
    ecosystem: Optional[str] = None
    package: Optional[str] = None
    epss_percentage: Optional[str] = None
    artifact_registry_url: Optional[str] = None
    artifact_registry: Optional[str] = None
    has: Optional[Any] = None
    scope: Optional[str] = None
    sort: Optional[str] = None
    direction: Optional[str] = None
    before: Optional[str] = None
    after: Optional[str] = None
    first: Optional[int] = None
    last: Optional[int] = None
    per_page: Optional[int] = None

class dependabot_list_org_secrets_params(msgspec.Struct):
    org: Optional[str] = None
    per_page: Optional[int] = None
    page: Optional[int] = None

class dependabot_get_org_public_key_params(msgspec.Struct):
    org: Optional[str] = None

class dependabot_get_org_secret_params(msgspec.Struct):
    org: Optional[str] = None
    secret_name: Optional[str] = None

class dependabot_create_or_update_org_secret_params(msgspec.Struct):
    org: Optional[str] = None
    secret_name: Optional[str] = None
    encrypted_value: Optional[Any] = None
    key_id: Optional[Any] = None
    visibility: Optional[Any] = None
    selected_repository_ids: Optional[Any] = None

class dependabot_delete_org_secret_params(msgspec.Struct):
    org: Optional[str] = None
    secret_name: Optional[str] = None

class dependabot_list_selected_repos_for_org_secret_params(msgspec.Struct):
    org: Optional[str] = None
    secret_name: Optional[str] = None
    page: Optional[int] = None
    per_page: Optional[int] = None

class dependabot_set_selected_repos_for_org_secret_params(msgspec.Struct):
    org: Optional[str] = None
    secret_name: Optional[str] = None
    selected_repository_ids: Optional[Any] = None

class dependabot_add_selected_repo_to_org_secret_params(msgspec.Struct):
    org: Optional[str] = None
    secret_name: Optional[str] = None
    repository_id: Optional[int] = None

class dependabot_remove_selected_repo_from_org_secret_params(msgspec.Struct):
    org: Optional[str] = None
    secret_name: Optional[str] = None
    repository_id: Optional[int] = None

class packages_list_docker_migration_conflicting_packages_for_organization_params(msgspec.Struct):
    org: Optional[str] = None

class activity_list_public_org_events_params(msgspec.Struct):
    org: Optional[str] = None
    per_page: Optional[int] = None
    page: Optional[int] = None

class orgs_list_failed_invitations_params(msgspec.Struct):
    org: Optional[str] = None
    per_page: Optional[int] = None
    page: Optional[int] = None

class orgs_list_webhooks_params(msgspec.Struct):
    org: Optional[str] = None
    per_page: Optional[int] = None
    page: Optional[int] = None

class orgs_create_webhook_params(msgspec.Struct):
    org: Optional[str] = None
    name: Optional[Any] = None
    config: Optional[Any] = None
    events: Optional[Any] = None
    active: Optional[Any] = None

class orgs_get_webhook_params(msgspec.Struct):
    org: Optional[str] = None
    hook_id: Optional[int] = None

class orgs_update_webhook_params(msgspec.Struct):
    org: Optional[str] = None
    hook_id: Optional[int] = None
    config: Optional[Any] = None
    events: Optional[Any] = None
    active: Optional[Any] = None
    name: Optional[Any] = None

class orgs_delete_webhook_params(msgspec.Struct):
    org: Optional[str] = None
    hook_id: Optional[int] = None

class orgs_get_webhook_config_for_org_params(msgspec.Struct):
    org: Optional[str] = None
    hook_id: Optional[int] = None

class orgs_update_webhook_config_for_org_params(msgspec.Struct):
    org: Optional[str] = None
    hook_id: Optional[int] = None
    url: Optional[Any] = None
    content_type: Optional[Any] = None
    secret: Optional[Any] = None
    insecure_ssl: Optional[Any] = None

class orgs_list_webhook_deliveries_params(msgspec.Struct):
    org: Optional[str] = None
    hook_id: Optional[int] = None
    per_page: Optional[int] = None
    cursor: Optional[str] = None

class orgs_get_webhook_delivery_params(msgspec.Struct):
    org: Optional[str] = None
    hook_id: Optional[int] = None
    delivery_id: Optional[int] = None

class orgs_redeliver_webhook_delivery_params(msgspec.Struct):
    org: Optional[str] = None
    hook_id: Optional[int] = None
    delivery_id: Optional[int] = None

class orgs_ping_webhook_params(msgspec.Struct):
    org: Optional[str] = None
    hook_id: Optional[int] = None

class api_insights_get_route_stats_by_actor_params(msgspec.Struct):
    org: Optional[str] = None
    actor_type: Optional[str] = None
    actor_id: Optional[int] = None
    min_timestamp: Optional[str] = None
    max_timestamp: Optional[str] = None
    page: Optional[int] = None
    per_page: Optional[int] = None
    direction: Optional[str] = None
    sort: Optional[List[str]] = None
    api_route_substring: Optional[str] = None

class api_insights_get_subject_stats_params(msgspec.Struct):
    org: Optional[str] = None
    min_timestamp: Optional[str] = None
    max_timestamp: Optional[str] = None
    page: Optional[int] = None
    per_page: Optional[int] = None
    direction: Optional[str] = None
    sort: Optional[List[str]] = None
    subject_name_substring: Optional[str] = None

class api_insights_get_summary_stats_params(msgspec.Struct):
    org: Optional[str] = None
    min_timestamp: Optional[str] = None
    max_timestamp: Optional[str] = None

class api_insights_get_summary_stats_by_user_params(msgspec.Struct):
    org: Optional[str] = None
    user_id: Optional[str] = None
    min_timestamp: Optional[str] = None
    max_timestamp: Optional[str] = None

class api_insights_get_summary_stats_by_actor_params(msgspec.Struct):
    org: Optional[str] = None
    min_timestamp: Optional[str] = None
    max_timestamp: Optional[str] = None
    actor_type: Optional[str] = None
    actor_id: Optional[int] = None

class api_insights_get_time_stats_params(msgspec.Struct):
    org: Optional[str] = None
    min_timestamp: Optional[str] = None
    max_timestamp: Optional[str] = None
    timestamp_increment: Optional[str] = None

class api_insights_get_time_stats_by_user_params(msgspec.Struct):
    org: Optional[str] = None
    user_id: Optional[str] = None
    min_timestamp: Optional[str] = None
    max_timestamp: Optional[str] = None
    timestamp_increment: Optional[str] = None

class api_insights_get_time_stats_by_actor_params(msgspec.Struct):
    org: Optional[str] = None
    actor_type: Optional[str] = None
    actor_id: Optional[int] = None
    min_timestamp: Optional[str] = None
    max_timestamp: Optional[str] = None
    timestamp_increment: Optional[str] = None

class api_insights_get_user_stats_params(msgspec.Struct):
    org: Optional[str] = None
    user_id: Optional[str] = None
    min_timestamp: Optional[str] = None
    max_timestamp: Optional[str] = None
    page: Optional[int] = None
    per_page: Optional[int] = None
    direction: Optional[str] = None
    sort: Optional[List[str]] = None
    actor_name_substring: Optional[str] = None

class apps_get_org_installation_params(msgspec.Struct):
    org: Optional[str] = None

class orgs_list_app_installations_params(msgspec.Struct):
    org: Optional[str] = None
    per_page: Optional[int] = None
    page: Optional[int] = None

class interactions_get_restrictions_for_org_params(msgspec.Struct):
    org: Optional[str] = None

class interactions_set_restrictions_for_org_params(msgspec.Struct):
    org: Optional[str] = None
    limit: Optional[Any] = None
    expiry: Optional[Any] = None

class interactions_remove_restrictions_for_org_params(msgspec.Struct):
    org: Optional[str] = None

class orgs_list_pending_invitations_params(msgspec.Struct):
    org: Optional[str] = None
    per_page: Optional[int] = None
    page: Optional[int] = None
    role: Optional[str] = None
    invitation_source: Optional[str] = None

class orgs_create_invitation_params(msgspec.Struct):
    org: Optional[str] = None
    invitee_id: Optional[Any] = None
    email: Optional[Any] = None
    role: Optional[Any] = None
    team_ids: Optional[Any] = None

class orgs_cancel_invitation_params(msgspec.Struct):
    org: Optional[str] = None
    invitation_id: Optional[int] = None

class orgs_list_invitation_teams_params(msgspec.Struct):
    org: Optional[str] = None
    invitation_id: Optional[int] = None
    per_page: Optional[int] = None
    page: Optional[int] = None

class orgs_list_issue_types_params(msgspec.Struct):
    org: Optional[str] = None

class orgs_create_issue_type_params(msgspec.Struct):
    org: Optional[str] = None
    name: Optional[Any] = None
    is_enabled: Optional[Any] = None
    description: Optional[Any] = None
    color: Optional[Any] = None

class orgs_update_issue_type_params(msgspec.Struct):
    org: Optional[str] = None
    issue_type_id: Optional[int] = None
    name: Optional[Any] = None
    is_enabled: Optional[Any] = None
    description: Optional[Any] = None
    color: Optional[Any] = None

class orgs_delete_issue_type_params(msgspec.Struct):
    org: Optional[str] = None
    issue_type_id: Optional[int] = None

class issues_list_for_org_params(msgspec.Struct):
    org: Optional[str] = None
    filter: Optional[str] = None
    state: Optional[str] = None
    labels: Optional[str] = None
    type: Optional[str] = None
    sort: Optional[str] = None
    direction: Optional[str] = None
    since: Optional[str] = None
    per_page: Optional[int] = None
    page: Optional[int] = None

class orgs_list_members_params(msgspec.Struct):
    org: Optional[str] = None
    filter: Optional[str] = None
    role: Optional[str] = None
    per_page: Optional[int] = None
    page: Optional[int] = None

class orgs_check_membership_for_user_params(msgspec.Struct):
    org: Optional[str] = None
    username: Optional[str] = None

class orgs_remove_member_params(msgspec.Struct):
    org: Optional[str] = None
    username: Optional[str] = None

class codespaces_get_codespaces_for_user_in_org_params(msgspec.Struct):
    per_page: Optional[int] = None
    page: Optional[int] = None
    org: Optional[str] = None
    username: Optional[str] = None

class codespaces_delete_from_organization_params(msgspec.Struct):
    org: Optional[str] = None
    username: Optional[str] = None
    codespace_name: Optional[str] = None

class codespaces_stop_in_organization_params(msgspec.Struct):
    org: Optional[str] = None
    username: Optional[str] = None
    codespace_name: Optional[str] = None

class copilot_get_copilot_seat_details_for_user_params(msgspec.Struct):
    org: Optional[str] = None
    username: Optional[str] = None

class orgs_get_membership_for_user_params(msgspec.Struct):
    org: Optional[str] = None
    username: Optional[str] = None

class orgs_set_membership_for_user_params(msgspec.Struct):
    org: Optional[str] = None
    username: Optional[str] = None
    role: Optional[Any] = None

class orgs_remove_membership_for_user_params(msgspec.Struct):
    org: Optional[str] = None
    username: Optional[str] = None

class migrations_list_for_org_params(msgspec.Struct):
    org: Optional[str] = None
    per_page: Optional[int] = None
    page: Optional[int] = None
    exclude: Optional[List[str]] = None

class migrations_start_for_org_params(msgspec.Struct):
    org: Optional[str] = None
    repositories: Optional[Any] = None
    lock_repositories: Optional[Any] = None
    exclude_metadata: Optional[Any] = None
    exclude_git_data: Optional[Any] = None
    exclude_attachments: Optional[Any] = None
    exclude_releases: Optional[Any] = None
    exclude_owner_projects: Optional[Any] = None
    org_metadata_only: Optional[Any] = None
    exclude: Optional[Any] = None

class migrations_get_status_for_org_params(msgspec.Struct):
    org: Optional[str] = None
    migration_id: Optional[int] = None
    exclude: Optional[List[str]] = None

class migrations_download_archive_for_org_params(msgspec.Struct):
    org: Optional[str] = None
    migration_id: Optional[int] = None

class migrations_delete_archive_for_org_params(msgspec.Struct):
    org: Optional[str] = None
    migration_id: Optional[int] = None

class migrations_unlock_repo_for_org_params(msgspec.Struct):
    org: Optional[str] = None
    migration_id: Optional[int] = None
    repo_name: Optional[str] = None

class migrations_list_repos_for_org_params(msgspec.Struct):
    org: Optional[str] = None
    migration_id: Optional[int] = None
    per_page: Optional[int] = None
    page: Optional[int] = None

class orgs_list_org_roles_params(msgspec.Struct):
    org: Optional[str] = None

class orgs_revoke_all_org_roles_team_params(msgspec.Struct):
    org: Optional[str] = None
    team_slug: Optional[str] = None

class orgs_assign_team_to_org_role_params(msgspec.Struct):
    org: Optional[str] = None
    team_slug: Optional[str] = None
    role_id: Optional[int] = None

class orgs_revoke_org_role_team_params(msgspec.Struct):
    org: Optional[str] = None
    team_slug: Optional[str] = None
    role_id: Optional[int] = None

class orgs_revoke_all_org_roles_user_params(msgspec.Struct):
    org: Optional[str] = None
    username: Optional[str] = None

class orgs_assign_user_to_org_role_params(msgspec.Struct):
    org: Optional[str] = None
    username: Optional[str] = None
    role_id: Optional[int] = None

class orgs_revoke_org_role_user_params(msgspec.Struct):
    org: Optional[str] = None
    username: Optional[str] = None
    role_id: Optional[int] = None

class orgs_get_org_role_params(msgspec.Struct):
    org: Optional[str] = None
    role_id: Optional[int] = None

class orgs_list_org_role_teams_params(msgspec.Struct):
    org: Optional[str] = None
    role_id: Optional[int] = None
    per_page: Optional[int] = None
    page: Optional[int] = None

class orgs_list_org_role_users_params(msgspec.Struct):
    org: Optional[str] = None
    role_id: Optional[int] = None
    per_page: Optional[int] = None
    page: Optional[int] = None

class orgs_list_outside_collaborators_params(msgspec.Struct):
    org: Optional[str] = None
    filter: Optional[str] = None
    per_page: Optional[int] = None
    page: Optional[int] = None

class orgs_convert_member_to_outside_collaborator_params(msgspec.Struct):
    org: Optional[str] = None
    username: Optional[str] = None
    async_: Optional[Any] = None

class orgs_remove_outside_collaborator_params(msgspec.Struct):
    org: Optional[str] = None
    username: Optional[str] = None

class packages_list_packages_for_organization_params(msgspec.Struct):
    package_type: Optional[str] = None
    org: Optional[str] = None
    visibility: Optional[str] = None
    page: Optional[int] = None
    per_page: Optional[int] = None

class packages_get_package_for_organization_params(msgspec.Struct):
    package_type: Optional[str] = None
    package_name: Optional[str] = None
    org: Optional[str] = None

class packages_delete_package_for_org_params(msgspec.Struct):
    package_type: Optional[str] = None
    package_name: Optional[str] = None
    org: Optional[str] = None

class packages_restore_package_for_org_params(msgspec.Struct):
    package_type: Optional[str] = None
    package_name: Optional[str] = None
    org: Optional[str] = None
    token: Optional[str] = None

class packages_get_all_package_versions_for_package_owned_by_org_params(msgspec.Struct):
    package_type: Optional[str] = None
    package_name: Optional[str] = None
    org: Optional[str] = None
    page: Optional[int] = None
    per_page: Optional[int] = None
    state: Optional[str] = None

class packages_get_package_version_for_organization_params(msgspec.Struct):
    package_type: Optional[str] = None
    package_name: Optional[str] = None
    org: Optional[str] = None
    package_version_id: Optional[int] = None

class packages_delete_package_version_for_org_params(msgspec.Struct):
    package_type: Optional[str] = None
    package_name: Optional[str] = None
    org: Optional[str] = None
    package_version_id: Optional[int] = None

class packages_restore_package_version_for_org_params(msgspec.Struct):
    package_type: Optional[str] = None
    package_name: Optional[str] = None
    org: Optional[str] = None
    package_version_id: Optional[int] = None

class orgs_list_pat_grant_requests_params(msgspec.Struct):
    org: Optional[str] = None
    per_page: Optional[int] = None
    page: Optional[int] = None
    sort: Optional[str] = None
    direction: Optional[str] = None
    owner: Optional[List[str]] = None
    repository: Optional[str] = None
    permission: Optional[str] = None
    last_used_before: Optional[str] = None
    last_used_after: Optional[str] = None
    token_id: Optional[List[str]] = None

class orgs_review_pat_grant_requests_in_bulk_params(msgspec.Struct):
    org: Optional[str] = None
    pat_request_ids: Optional[Any] = None
    action: Optional[Any] = None
    reason: Optional[Any] = None

class orgs_review_pat_grant_request_params(msgspec.Struct):
    org: Optional[str] = None
    pat_request_id: Optional[int] = None
    action: Optional[Any] = None
    reason: Optional[Any] = None

class orgs_list_pat_grant_request_repositories_params(msgspec.Struct):
    org: Optional[str] = None
    pat_request_id: Optional[int] = None
    per_page: Optional[int] = None
    page: Optional[int] = None

class orgs_list_pat_grants_params(msgspec.Struct):
    org: Optional[str] = None
    per_page: Optional[int] = None
    page: Optional[int] = None
    sort: Optional[str] = None
    direction: Optional[str] = None
    owner: Optional[List[str]] = None
    repository: Optional[str] = None
    permission: Optional[str] = None
    last_used_before: Optional[str] = None
    last_used_after: Optional[str] = None
    token_id: Optional[List[str]] = None

class orgs_update_pat_accesses_params(msgspec.Struct):
    org: Optional[str] = None
    action: Optional[Any] = None
    pat_ids: Optional[Any] = None

class orgs_update_pat_access_params(msgspec.Struct):
    org: Optional[str] = None
    pat_id: Optional[int] = None
    action: Optional[Any] = None

class orgs_list_pat_grant_repositories_params(msgspec.Struct):
    org: Optional[str] = None
    pat_id: Optional[int] = None
    per_page: Optional[int] = None
    page: Optional[int] = None

class private_registries_list_org_private_registries_params(msgspec.Struct):
    org: Optional[str] = None
    per_page: Optional[int] = None
    page: Optional[int] = None

class private_registries_create_org_private_registry_params(msgspec.Struct):
    org: Optional[str] = None
    registry_type: Optional[Any] = None
    url: Optional[Any] = None
    username: Optional[Any] = None
    encrypted_value: Optional[Any] = None
    key_id: Optional[Any] = None
    visibility: Optional[Any] = None
    selected_repository_ids: Optional[Any] = None

class private_registries_get_org_public_key_params(msgspec.Struct):
    org: Optional[str] = None

class private_registries_get_org_private_registry_params(msgspec.Struct):
    org: Optional[str] = None
    secret_name: Optional[str] = None

class private_registries_update_org_private_registry_params(msgspec.Struct):
    org: Optional[str] = None
    secret_name: Optional[str] = None
    registry_type: Optional[Any] = None
    url: Optional[Any] = None
    username: Optional[Any] = None
    encrypted_value: Optional[Any] = None
    key_id: Optional[Any] = None
    visibility: Optional[Any] = None
    selected_repository_ids: Optional[Any] = None

class private_registries_delete_org_private_registry_params(msgspec.Struct):
    org: Optional[str] = None
    secret_name: Optional[str] = None

class projects_classic_list_for_org_params(msgspec.Struct):
    org: Optional[str] = None
    state: Optional[str] = None
    per_page: Optional[int] = None
    page: Optional[int] = None

class projects_classic_create_for_org_params(msgspec.Struct):
    org: Optional[str] = None
    name: Optional[Any] = None
    body: Optional[Any] = None

class orgs_get_all_custom_properties_params(msgspec.Struct):
    org: Optional[str] = None

class orgs_create_or_update_custom_properties_params(msgspec.Struct):
    org: Optional[str] = None
    properties: Optional[Any] = None

class orgs_get_custom_property_params(msgspec.Struct):
    org: Optional[str] = None
    custom_property_name: Optional[str] = None

class orgs_create_or_update_custom_property_params(msgspec.Struct):
    org: Optional[str] = None
    custom_property_name: Optional[str] = None
    value_type: Optional[Any] = None
    required: Optional[Any] = None
    default_value: Optional[Any] = None
    description: Optional[Any] = None
    allowed_values: Optional[Any] = None
    values_editable_by: Optional[Any] = None

class orgs_remove_custom_property_params(msgspec.Struct):
    org: Optional[str] = None
    custom_property_name: Optional[str] = None

class orgs_list_custom_properties_values_for_repos_params(msgspec.Struct):
    org: Optional[str] = None
    per_page: Optional[int] = None
    page: Optional[int] = None
    repository_query: Optional[str] = None

class orgs_create_or_update_custom_properties_values_for_repos_params(msgspec.Struct):
    org: Optional[str] = None
    repository_names: Optional[Any] = None
    properties: Optional[Any] = None

class orgs_list_public_members_params(msgspec.Struct):
    org: Optional[str] = None
    per_page: Optional[int] = None
    page: Optional[int] = None

class orgs_check_public_membership_for_user_params(msgspec.Struct):
    org: Optional[str] = None
    username: Optional[str] = None

class orgs_set_public_membership_for_authenticated_user_params(msgspec.Struct):
    org: Optional[str] = None
    username: Optional[str] = None

class orgs_remove_public_membership_for_authenticated_user_params(msgspec.Struct):
    org: Optional[str] = None
    username: Optional[str] = None

class repos_list_for_org_params(msgspec.Struct):
    org: Optional[str] = None
    type: Optional[str] = None
    sort: Optional[str] = None
    direction: Optional[str] = None
    per_page: Optional[int] = None
    page: Optional[int] = None

class repos_create_in_org_params(msgspec.Struct):
    org: Optional[str] = None
    name: Optional[Any] = None
    description: Optional[Any] = None
    homepage: Optional[Any] = None
    private: Optional[Any] = None
    visibility: Optional[Any] = None
    has_issues: Optional[Any] = None
    has_projects: Optional[Any] = None
    has_wiki: Optional[Any] = None
    has_downloads: Optional[Any] = None
    is_template: Optional[Any] = None
    team_id: Optional[Any] = None
    auto_init: Optional[Any] = None
    gitignore_template: Optional[Any] = None
    license_template: Optional[Any] = None
    allow_squash_merge: Optional[Any] = None
    allow_merge_commit: Optional[Any] = None
    allow_rebase_merge: Optional[Any] = None
    allow_auto_merge: Optional[Any] = None
    delete_branch_on_merge: Optional[Any] = None
    use_squash_pr_title_as_default: Optional[Any] = None
    squash_merge_commit_title: Optional[Any] = None
    squash_merge_commit_message: Optional[Any] = None
    merge_commit_title: Optional[Any] = None
    merge_commit_message: Optional[Any] = None
    custom_properties: Optional[Any] = None

class repos_get_org_rulesets_params(msgspec.Struct):
    org: Optional[str] = None
    per_page: Optional[int] = None
    page: Optional[int] = None
    targets: Optional[str] = None

class repos_create_org_ruleset_params(msgspec.Struct):
    org: Optional[str] = None
    name: Optional[Any] = None
    target: Optional[Any] = None
    enforcement: Optional[Any] = None
    bypass_actors: Optional[Any] = None
    conditions: Optional[Any] = None
    rules: Optional[Any] = None

class repos_get_org_rule_suites_params(msgspec.Struct):
    org: Optional[str] = None
    ref: Optional[str] = None
    repository_name: Optional[str] = None
    time_period: Optional[str] = None
    actor_name: Optional[str] = None
    rule_suite_result: Optional[str] = None
    per_page: Optional[int] = None
    page: Optional[int] = None

class repos_get_org_rule_suite_params(msgspec.Struct):
    org: Optional[str] = None
    rule_suite_id: Optional[int] = None

class repos_get_org_ruleset_params(msgspec.Struct):
    org: Optional[str] = None
    ruleset_id: Optional[int] = None

class repos_update_org_ruleset_params(msgspec.Struct):
    org: Optional[str] = None
    ruleset_id: Optional[int] = None
    name: Optional[Any] = None
    target: Optional[Any] = None
    enforcement: Optional[Any] = None
    bypass_actors: Optional[Any] = None
    conditions: Optional[Any] = None
    rules: Optional[Any] = None

class repos_delete_org_ruleset_params(msgspec.Struct):
    org: Optional[str] = None
    ruleset_id: Optional[int] = None

class orgs_get_org_ruleset_history_params(msgspec.Struct):
    org: Optional[str] = None
    per_page: Optional[int] = None
    page: Optional[int] = None
    ruleset_id: Optional[int] = None

class orgs_get_org_ruleset_version_params(msgspec.Struct):
    org: Optional[str] = None
    ruleset_id: Optional[int] = None
    version_id: Optional[int] = None

class secret_scanning_list_alerts_for_org_params(msgspec.Struct):
    org: Optional[str] = None
    state: Optional[str] = None
    secret_type: Optional[str] = None
    resolution: Optional[str] = None
    sort: Optional[str] = None
    direction: Optional[str] = None
    page: Optional[int] = None
    per_page: Optional[int] = None
    before: Optional[str] = None
    after: Optional[str] = None
    validity: Optional[str] = None
    is_publicly_leaked: Optional[bool] = None
    is_multi_repo: Optional[bool] = None
    hide_secret: Optional[bool] = None

class secret_scanning_list_org_pattern_configs_params(msgspec.Struct):
    org: Optional[str] = None

class secret_scanning_update_org_pattern_configs_params(msgspec.Struct):
    org: Optional[str] = None
    pattern_config_version: Optional[Any] = None
    provider_pattern_settings: Optional[Any] = None
    custom_pattern_settings: Optional[Any] = None

class security_advisories_list_org_repository_advisories_params(msgspec.Struct):
    org: Optional[str] = None
    direction: Optional[str] = None
    sort: Optional[str] = None
    before: Optional[str] = None
    after: Optional[str] = None
    per_page: Optional[int] = None
    state: Optional[str] = None

class orgs_list_security_manager_teams_params(msgspec.Struct):
    org: Optional[str] = None

class orgs_add_security_manager_team_params(msgspec.Struct):
    org: Optional[str] = None
    team_slug: Optional[str] = None

class orgs_remove_security_manager_team_params(msgspec.Struct):
    org: Optional[str] = None
    team_slug: Optional[str] = None

class billing_get_github_actions_billing_org_params(msgspec.Struct):
    org: Optional[str] = None

class billing_get_github_packages_billing_org_params(msgspec.Struct):
    org: Optional[str] = None

class billing_get_shared_storage_billing_org_params(msgspec.Struct):
    org: Optional[str] = None

class hosted_compute_list_network_configurations_for_org_params(msgspec.Struct):
    org: Optional[str] = None
    per_page: Optional[int] = None
    page: Optional[int] = None

class hosted_compute_create_network_configuration_for_org_params(msgspec.Struct):
    org: Optional[str] = None
    name: Optional[Any] = None
    compute_service: Optional[Any] = None
    network_settings_ids: Optional[Any] = None

class hosted_compute_get_network_configuration_for_org_params(msgspec.Struct):
    org: Optional[str] = None
    network_configuration_id: Optional[str] = None

class hosted_compute_update_network_configuration_for_org_params(msgspec.Struct):
    org: Optional[str] = None
    network_configuration_id: Optional[str] = None
    name: Optional[Any] = None
    compute_service: Optional[Any] = None
    network_settings_ids: Optional[Any] = None

class hosted_compute_delete_network_configuration_from_org_params(msgspec.Struct):
    org: Optional[str] = None
    network_configuration_id: Optional[str] = None

class hosted_compute_get_network_settings_for_org_params(msgspec.Struct):
    org: Optional[str] = None
    network_settings_id: Optional[str] = None

class copilot_copilot_metrics_for_team_params(msgspec.Struct):
    org: Optional[str] = None
    team_slug: Optional[str] = None
    since: Optional[str] = None
    until: Optional[str] = None
    page: Optional[int] = None
    per_page: Optional[int] = None

class teams_list_params(msgspec.Struct):
    org: Optional[str] = None
    per_page: Optional[int] = None
    page: Optional[int] = None

class teams_create_params(msgspec.Struct):
    org: Optional[str] = None
    name: Optional[Any] = None
    description: Optional[Any] = None
    maintainers: Optional[Any] = None
    repo_names: Optional[Any] = None
    privacy: Optional[Any] = None
    notification_setting: Optional[Any] = None
    permission: Optional[Any] = None
    parent_team_id: Optional[Any] = None

class teams_get_by_name_params(msgspec.Struct):
    org: Optional[str] = None
    team_slug: Optional[str] = None

class teams_update_in_org_params(msgspec.Struct):
    org: Optional[str] = None
    team_slug: Optional[str] = None
    name: Optional[Any] = None
    description: Optional[Any] = None
    privacy: Optional[Any] = None
    notification_setting: Optional[Any] = None
    permission: Optional[Any] = None
    parent_team_id: Optional[Any] = None

class teams_delete_in_org_params(msgspec.Struct):
    org: Optional[str] = None
    team_slug: Optional[str] = None

class teams_list_discussions_in_org_params(msgspec.Struct):
    org: Optional[str] = None
    team_slug: Optional[str] = None
    direction: Optional[str] = None
    per_page: Optional[int] = None
    page: Optional[int] = None
    pinned: Optional[str] = None

class teams_create_discussion_in_org_params(msgspec.Struct):
    org: Optional[str] = None
    team_slug: Optional[str] = None
    title: Optional[Any] = None
    body: Optional[Any] = None
    private: Optional[Any] = None

class teams_get_discussion_in_org_params(msgspec.Struct):
    org: Optional[str] = None
    team_slug: Optional[str] = None
    discussion_number: Optional[int] = None

class teams_update_discussion_in_org_params(msgspec.Struct):
    org: Optional[str] = None
    team_slug: Optional[str] = None
    discussion_number: Optional[int] = None
    title: Optional[Any] = None
    body: Optional[Any] = None

class teams_delete_discussion_in_org_params(msgspec.Struct):
    org: Optional[str] = None
    team_slug: Optional[str] = None
    discussion_number: Optional[int] = None

class teams_list_discussion_comments_in_org_params(msgspec.Struct):
    org: Optional[str] = None
    team_slug: Optional[str] = None
    discussion_number: Optional[int] = None
    direction: Optional[str] = None
    per_page: Optional[int] = None
    page: Optional[int] = None

class teams_create_discussion_comment_in_org_params(msgspec.Struct):
    org: Optional[str] = None
    team_slug: Optional[str] = None
    discussion_number: Optional[int] = None
    body: Optional[Any] = None

class teams_get_discussion_comment_in_org_params(msgspec.Struct):
    org: Optional[str] = None
    team_slug: Optional[str] = None
    discussion_number: Optional[int] = None
    comment_number: Optional[int] = None

class teams_update_discussion_comment_in_org_params(msgspec.Struct):
    org: Optional[str] = None
    team_slug: Optional[str] = None
    discussion_number: Optional[int] = None
    comment_number: Optional[int] = None
    body: Optional[Any] = None

class teams_delete_discussion_comment_in_org_params(msgspec.Struct):
    org: Optional[str] = None
    team_slug: Optional[str] = None
    discussion_number: Optional[int] = None
    comment_number: Optional[int] = None

class reactions_list_for_team_discussion_comment_in_org_params(msgspec.Struct):
    org: Optional[str] = None
    team_slug: Optional[str] = None
    discussion_number: Optional[int] = None
    comment_number: Optional[int] = None
    content: Optional[str] = None
    per_page: Optional[int] = None
    page: Optional[int] = None

class reactions_create_for_team_discussion_comment_in_org_params(msgspec.Struct):
    org: Optional[str] = None
    team_slug: Optional[str] = None
    discussion_number: Optional[int] = None
    comment_number: Optional[int] = None
    content: Optional[Any] = None

class reactions_delete_for_team_discussion_comment_params(msgspec.Struct):
    org: Optional[str] = None
    team_slug: Optional[str] = None
    discussion_number: Optional[int] = None
    comment_number: Optional[int] = None
    reaction_id: Optional[int] = None

class reactions_list_for_team_discussion_in_org_params(msgspec.Struct):
    org: Optional[str] = None
    team_slug: Optional[str] = None
    discussion_number: Optional[int] = None
    content: Optional[str] = None
    per_page: Optional[int] = None
    page: Optional[int] = None

class reactions_create_for_team_discussion_in_org_params(msgspec.Struct):
    org: Optional[str] = None
    team_slug: Optional[str] = None
    discussion_number: Optional[int] = None
    content: Optional[Any] = None

class reactions_delete_for_team_discussion_params(msgspec.Struct):
    org: Optional[str] = None
    team_slug: Optional[str] = None
    discussion_number: Optional[int] = None
    reaction_id: Optional[int] = None

class teams_list_pending_invitations_in_org_params(msgspec.Struct):
    org: Optional[str] = None
    team_slug: Optional[str] = None
    per_page: Optional[int] = None
    page: Optional[int] = None

class teams_list_members_in_org_params(msgspec.Struct):
    org: Optional[str] = None
    team_slug: Optional[str] = None
    role: Optional[str] = None
    per_page: Optional[int] = None
    page: Optional[int] = None

class teams_get_membership_for_user_in_org_params(msgspec.Struct):
    org: Optional[str] = None
    team_slug: Optional[str] = None
    username: Optional[str] = None

class teams_add_or_update_membership_for_user_in_org_params(msgspec.Struct):
    org: Optional[str] = None
    team_slug: Optional[str] = None
    username: Optional[str] = None
    role: Optional[Any] = None

class teams_remove_membership_for_user_in_org_params(msgspec.Struct):
    org: Optional[str] = None
    team_slug: Optional[str] = None
    username: Optional[str] = None

class teams_list_projects_in_org_params(msgspec.Struct):
    org: Optional[str] = None
    team_slug: Optional[str] = None
    per_page: Optional[int] = None
    page: Optional[int] = None

class teams_check_permissions_for_project_in_org_params(msgspec.Struct):
    org: Optional[str] = None
    team_slug: Optional[str] = None
    project_id: Optional[int] = None

class teams_add_or_update_project_permissions_in_org_params(msgspec.Struct):
    org: Optional[str] = None
    team_slug: Optional[str] = None
    project_id: Optional[int] = None
    permission: Optional[Any] = None

class teams_remove_project_in_org_params(msgspec.Struct):
    org: Optional[str] = None
    team_slug: Optional[str] = None
    project_id: Optional[int] = None

class teams_list_repos_in_org_params(msgspec.Struct):
    org: Optional[str] = None
    team_slug: Optional[str] = None
    per_page: Optional[int] = None
    page: Optional[int] = None

class teams_check_permissions_for_repo_in_org_params(msgspec.Struct):
    org: Optional[str] = None
    team_slug: Optional[str] = None
    owner: Optional[str] = None
    repo: Optional[str] = None

class teams_add_or_update_repo_permissions_in_org_params(msgspec.Struct):
    org: Optional[str] = None
    team_slug: Optional[str] = None
    owner: Optional[str] = None
    repo: Optional[str] = None
    permission: Optional[Any] = None

class teams_remove_repo_in_org_params(msgspec.Struct):
    org: Optional[str] = None
    team_slug: Optional[str] = None
    owner: Optional[str] = None
    repo: Optional[str] = None

class teams_list_child_in_org_params(msgspec.Struct):
    org: Optional[str] = None
    team_slug: Optional[str] = None
    per_page: Optional[int] = None
    page: Optional[int] = None

class orgs_enable_or_disable_security_product_on_all_org_repos_params(msgspec.Struct):
    org: Optional[str] = None
    security_product: Optional[str] = None
    enablement: Optional[str] = None
    query_suite: Optional[Any] = None

class projects_classic_get_card_params(msgspec.Struct):
    card_id: Optional[int] = None

class projects_classic_update_card_params(msgspec.Struct):
    card_id: Optional[int] = None
    note: Optional[Any] = None
    archived: Optional[Any] = None

class projects_classic_delete_card_params(msgspec.Struct):
    card_id: Optional[int] = None

class projects_classic_move_card_params(msgspec.Struct):
    card_id: Optional[int] = None
    position: Optional[Any] = None
    column_id: Optional[Any] = None

class projects_classic_get_column_params(msgspec.Struct):
    column_id: Optional[int] = None

class projects_classic_update_column_params(msgspec.Struct):
    column_id: Optional[int] = None
    name: Optional[Any] = None

class projects_classic_delete_column_params(msgspec.Struct):
    column_id: Optional[int] = None

class projects_classic_list_cards_params(msgspec.Struct):
    column_id: Optional[int] = None
    archived_state: Optional[str] = None
    per_page: Optional[int] = None
    page: Optional[int] = None

class projects_classic_create_card_params(msgspec.Struct):
    column_id: Optional[int] = None

class projects_classic_move_column_params(msgspec.Struct):
    column_id: Optional[int] = None
    position: Optional[Any] = None

class projects_classic_get_params(msgspec.Struct):
    project_id: Optional[int] = None

class projects_classic_update_params(msgspec.Struct):
    project_id: Optional[int] = None
    name: Optional[Any] = None
    body: Optional[Any] = None
    state: Optional[Any] = None
    organization_permission: Optional[Any] = None
    private: Optional[Any] = None

class projects_classic_delete_params(msgspec.Struct):
    project_id: Optional[int] = None

class projects_classic_list_collaborators_params(msgspec.Struct):
    project_id: Optional[int] = None
    affiliation: Optional[str] = None
    per_page: Optional[int] = None
    page: Optional[int] = None

class projects_classic_add_collaborator_params(msgspec.Struct):
    project_id: Optional[int] = None
    username: Optional[str] = None
    permission: Optional[Any] = None

class projects_classic_remove_collaborator_params(msgspec.Struct):
    project_id: Optional[int] = None
    username: Optional[str] = None

class projects_classic_get_permission_for_user_params(msgspec.Struct):
    project_id: Optional[int] = None
    username: Optional[str] = None

class projects_classic_list_columns_params(msgspec.Struct):
    project_id: Optional[int] = None
    per_page: Optional[int] = None
    page: Optional[int] = None

class projects_classic_create_column_params(msgspec.Struct):
    project_id: Optional[int] = None
    name: Optional[Any] = None

class rate_limit_get_params(msgspec.Struct):
    pass

class repos_get_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None

class repos_update_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    name: Optional[Any] = None
    description: Optional[Any] = None
    homepage: Optional[Any] = None
    private: Optional[Any] = None
    visibility: Optional[Any] = None
    security_and_analysis: Optional[Any] = None
    has_issues: Optional[Any] = None
    has_projects: Optional[Any] = None
    has_wiki: Optional[Any] = None
    is_template: Optional[Any] = None
    default_branch: Optional[Any] = None
    allow_squash_merge: Optional[Any] = None
    allow_merge_commit: Optional[Any] = None
    allow_rebase_merge: Optional[Any] = None
    allow_auto_merge: Optional[Any] = None
    delete_branch_on_merge: Optional[Any] = None
    allow_update_branch: Optional[Any] = None
    use_squash_pr_title_as_default: Optional[Any] = None
    squash_merge_commit_title: Optional[Any] = None
    squash_merge_commit_message: Optional[Any] = None
    merge_commit_title: Optional[Any] = None
    merge_commit_message: Optional[Any] = None
    archived: Optional[Any] = None
    allow_forking: Optional[Any] = None
    web_commit_signoff_required: Optional[Any] = None

class repos_delete_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None

class actions_list_artifacts_for_repo_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    per_page: Optional[int] = None
    page: Optional[int] = None
    name: Optional[str] = None

class actions_get_artifact_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    artifact_id: Optional[int] = None

class actions_delete_artifact_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    artifact_id: Optional[int] = None

class actions_download_artifact_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    artifact_id: Optional[int] = None
    archive_format: Optional[str] = None

class actions_get_actions_cache_usage_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None

class actions_get_actions_cache_list_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    per_page: Optional[int] = None
    page: Optional[int] = None
    ref: Optional[str] = None
    key: Optional[str] = None
    sort: Optional[str] = None
    direction: Optional[str] = None

class actions_delete_actions_cache_by_key_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    key: Optional[str] = None
    ref: Optional[str] = None

class actions_delete_actions_cache_by_id_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    cache_id: Optional[int] = None

class actions_get_job_for_workflow_run_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    job_id: Optional[int] = None

class actions_download_job_logs_for_workflow_run_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    job_id: Optional[int] = None

class actions_re_run_job_for_workflow_run_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    job_id: Optional[int] = None
    enable_debug_logging: Optional[Any] = None

class actions_get_custom_oidc_sub_claim_for_repo_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None

class actions_set_custom_oidc_sub_claim_for_repo_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    use_default: Optional[Any] = None
    include_claim_keys: Optional[Any] = None

class actions_list_repo_organization_secrets_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    per_page: Optional[int] = None
    page: Optional[int] = None

class actions_list_repo_organization_variables_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    per_page: Optional[int] = None
    page: Optional[int] = None

class actions_get_github_actions_permissions_repository_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None

class actions_set_github_actions_permissions_repository_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    enabled: Optional[Any] = None
    allowed_actions: Optional[Any] = None
    sha_pinning_required: Optional[Any] = None

class actions_get_workflow_access_to_repository_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None

class actions_set_workflow_access_to_repository_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    access_level: Optional[Any] = None

class actions_get_artifact_and_log_retention_settings_repository_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None

class actions_set_artifact_and_log_retention_settings_repository_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    days: Optional[Any] = None

class actions_get_fork_pr_contributor_approval_permissions_repository_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None

class actions_set_fork_pr_contributor_approval_permissions_repository_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    approval_policy: Optional[Any] = None

class actions_get_private_repo_fork_pr_workflows_settings_repository_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None

class actions_set_private_repo_fork_pr_workflows_settings_repository_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    run_workflows_from_fork_pull_requests: Optional[Any] = None
    send_write_tokens_to_workflows: Optional[Any] = None
    send_secrets_and_variables: Optional[Any] = None
    require_approval_for_fork_pr_workflows: Optional[Any] = None

class actions_get_allowed_actions_repository_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None

class actions_set_allowed_actions_repository_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    github_owned_allowed: Optional[Any] = None
    verified_allowed: Optional[Any] = None
    patterns_allowed: Optional[Any] = None

class actions_get_github_actions_default_workflow_permissions_repository_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None

class actions_set_github_actions_default_workflow_permissions_repository_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    default_workflow_permissions: Optional[Any] = None
    can_approve_pull_request_reviews: Optional[Any] = None

class actions_list_self_hosted_runners_for_repo_params(msgspec.Struct):
    name: Optional[str] = None
    owner: Optional[str] = None
    repo: Optional[str] = None
    per_page: Optional[int] = None
    page: Optional[int] = None

class actions_list_runner_applications_for_repo_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None

class actions_generate_runner_jitconfig_for_repo_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    name: Optional[Any] = None
    runner_group_id: Optional[Any] = None
    labels: Optional[Any] = None
    work_folder: Optional[Any] = None

class actions_create_registration_token_for_repo_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None

class actions_create_remove_token_for_repo_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None

class actions_get_self_hosted_runner_for_repo_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    runner_id: Optional[int] = None

class actions_delete_self_hosted_runner_from_repo_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    runner_id: Optional[int] = None

class actions_list_labels_for_self_hosted_runner_for_repo_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    runner_id: Optional[int] = None

class actions_add_custom_labels_to_self_hosted_runner_for_repo_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    runner_id: Optional[int] = None
    labels: Optional[Any] = None

class actions_set_custom_labels_for_self_hosted_runner_for_repo_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    runner_id: Optional[int] = None
    labels: Optional[Any] = None

class actions_remove_all_custom_labels_from_self_hosted_runner_for_repo_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    runner_id: Optional[int] = None

class actions_remove_custom_label_from_self_hosted_runner_for_repo_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    runner_id: Optional[int] = None
    name: Optional[str] = None

class actions_list_workflow_runs_for_repo_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    actor: Optional[str] = None
    branch: Optional[str] = None
    event: Optional[str] = None
    status: Optional[str] = None
    per_page: Optional[int] = None
    page: Optional[int] = None
    created: Optional[str] = None
    exclude_pull_requests: Optional[bool] = None
    check_suite_id: Optional[int] = None
    head_sha: Optional[str] = None

class actions_get_workflow_run_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    run_id: Optional[int] = None
    exclude_pull_requests: Optional[bool] = None

class actions_delete_workflow_run_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    run_id: Optional[int] = None

class actions_get_reviews_for_run_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    run_id: Optional[int] = None

class actions_approve_workflow_run_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    run_id: Optional[int] = None

class actions_list_workflow_run_artifacts_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    run_id: Optional[int] = None
    per_page: Optional[int] = None
    page: Optional[int] = None
    name: Optional[str] = None

class actions_get_workflow_run_attempt_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    run_id: Optional[int] = None
    attempt_number: Optional[int] = None
    exclude_pull_requests: Optional[bool] = None

class actions_list_jobs_for_workflow_run_attempt_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    run_id: Optional[int] = None
    attempt_number: Optional[int] = None
    per_page: Optional[int] = None
    page: Optional[int] = None

class actions_download_workflow_run_attempt_logs_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    run_id: Optional[int] = None
    attempt_number: Optional[int] = None

class actions_cancel_workflow_run_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    run_id: Optional[int] = None

class actions_review_custom_gates_for_run_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    run_id: Optional[int] = None

class actions_force_cancel_workflow_run_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    run_id: Optional[int] = None

class actions_list_jobs_for_workflow_run_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    run_id: Optional[int] = None
    filter: Optional[str] = None
    per_page: Optional[int] = None
    page: Optional[int] = None

class actions_download_workflow_run_logs_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    run_id: Optional[int] = None

class actions_delete_workflow_run_logs_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    run_id: Optional[int] = None

class actions_get_pending_deployments_for_run_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    run_id: Optional[int] = None

class actions_review_pending_deployments_for_run_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    run_id: Optional[int] = None
    environment_ids: Optional[Any] = None
    state: Optional[Any] = None
    comment: Optional[Any] = None

class actions_re_run_workflow_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    run_id: Optional[int] = None
    enable_debug_logging: Optional[Any] = None

class actions_re_run_workflow_failed_jobs_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    run_id: Optional[int] = None
    enable_debug_logging: Optional[Any] = None

class actions_get_workflow_run_usage_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    run_id: Optional[int] = None

class actions_list_repo_secrets_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    per_page: Optional[int] = None
    page: Optional[int] = None

class actions_get_repo_public_key_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None

class actions_get_repo_secret_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    secret_name: Optional[str] = None

class actions_create_or_update_repo_secret_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    secret_name: Optional[str] = None
    encrypted_value: Optional[Any] = None
    key_id: Optional[Any] = None

class actions_delete_repo_secret_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    secret_name: Optional[str] = None

class actions_list_repo_variables_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    per_page: Optional[int] = None
    page: Optional[int] = None

class actions_create_repo_variable_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    name: Optional[Any] = None
    value: Optional[Any] = None

class actions_get_repo_variable_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    name: Optional[str] = None

class actions_update_repo_variable_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    name: Optional[str] = None
    name_: Optional[Any] = None
    value: Optional[Any] = None

class actions_delete_repo_variable_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    name: Optional[str] = None

class actions_list_repo_workflows_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    per_page: Optional[int] = None
    page: Optional[int] = None

class actions_get_workflow_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    workflow_id: Optional[Any] = None

class actions_disable_workflow_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    workflow_id: Optional[Any] = None

class actions_create_workflow_dispatch_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    workflow_id: Optional[Any] = None
    ref: Optional[Any] = None
    inputs: Optional[Any] = None

class actions_enable_workflow_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    workflow_id: Optional[Any] = None

class actions_list_workflow_runs_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    workflow_id: Optional[Any] = None
    actor: Optional[str] = None
    branch: Optional[str] = None
    event: Optional[str] = None
    status: Optional[str] = None
    per_page: Optional[int] = None
    page: Optional[int] = None
    created: Optional[str] = None
    exclude_pull_requests: Optional[bool] = None
    check_suite_id: Optional[int] = None
    head_sha: Optional[str] = None

class actions_get_workflow_usage_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    workflow_id: Optional[Any] = None

class repos_list_activities_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    direction: Optional[str] = None
    per_page: Optional[int] = None
    before: Optional[str] = None
    after: Optional[str] = None
    ref: Optional[str] = None
    actor: Optional[str] = None
    time_period: Optional[str] = None
    activity_type: Optional[str] = None

class issues_list_assignees_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    per_page: Optional[int] = None
    page: Optional[int] = None

class issues_check_user_can_be_assigned_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    assignee: Optional[str] = None

class repos_create_attestation_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    bundle: Optional[Any] = None

class repos_list_attestations_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    per_page: Optional[int] = None
    before: Optional[str] = None
    after: Optional[str] = None
    subject_digest: Optional[str] = None
    predicate_type: Optional[str] = None

class repos_list_autolinks_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None

class repos_create_autolink_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    key_prefix: Optional[Any] = None
    url_template: Optional[Any] = None
    is_alphanumeric: Optional[Any] = None

class repos_get_autolink_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    autolink_id: Optional[int] = None

class repos_delete_autolink_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    autolink_id: Optional[int] = None

class repos_check_automated_security_fixes_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None

class repos_enable_automated_security_fixes_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None

class repos_disable_automated_security_fixes_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None

class repos_list_branches_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    protected: Optional[bool] = None
    per_page: Optional[int] = None
    page: Optional[int] = None

class repos_get_branch_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    branch: Optional[str] = None

class repos_get_branch_protection_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    branch: Optional[str] = None

class repos_update_branch_protection_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    branch: Optional[str] = None
    required_status_checks: Optional[Any] = None
    enforce_admins: Optional[Any] = None
    required_pull_request_reviews: Optional[Any] = None
    restrictions: Optional[Any] = None
    required_linear_history: Optional[Any] = None
    allow_force_pushes: Optional[Any] = None
    allow_deletions: Optional[Any] = None
    block_creations: Optional[Any] = None
    required_conversation_resolution: Optional[Any] = None
    lock_branch: Optional[Any] = None
    allow_fork_syncing: Optional[Any] = None

class repos_delete_branch_protection_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    branch: Optional[str] = None

class repos_get_admin_branch_protection_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    branch: Optional[str] = None

class repos_set_admin_branch_protection_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    branch: Optional[str] = None

class repos_delete_admin_branch_protection_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    branch: Optional[str] = None

class repos_get_pull_request_review_protection_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    branch: Optional[str] = None

class repos_update_pull_request_review_protection_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    branch: Optional[str] = None
    dismissal_restrictions: Optional[Any] = None
    dismiss_stale_reviews: Optional[Any] = None
    require_code_owner_reviews: Optional[Any] = None
    required_approving_review_count: Optional[Any] = None
    require_last_push_approval: Optional[Any] = None
    bypass_pull_request_allowances: Optional[Any] = None

class repos_delete_pull_request_review_protection_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    branch: Optional[str] = None

class repos_get_commit_signature_protection_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    branch: Optional[str] = None

class repos_create_commit_signature_protection_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    branch: Optional[str] = None

class repos_delete_commit_signature_protection_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    branch: Optional[str] = None

class repos_get_status_checks_protection_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    branch: Optional[str] = None

class repos_update_status_check_protection_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    branch: Optional[str] = None
    strict: Optional[Any] = None
    contexts: Optional[Any] = None
    checks: Optional[Any] = None

class repos_remove_status_check_protection_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    branch: Optional[str] = None

class repos_get_all_status_check_contexts_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    branch: Optional[str] = None

class repos_add_status_check_contexts_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    branch: Optional[str] = None

class repos_set_status_check_contexts_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    branch: Optional[str] = None

class repos_remove_status_check_contexts_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    branch: Optional[str] = None

class repos_get_access_restrictions_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    branch: Optional[str] = None

class repos_delete_access_restrictions_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    branch: Optional[str] = None

class repos_get_apps_with_access_to_protected_branch_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    branch: Optional[str] = None

class repos_add_app_access_restrictions_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    branch: Optional[str] = None
    apps: Optional[Any] = None

class repos_set_app_access_restrictions_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    branch: Optional[str] = None
    apps: Optional[Any] = None

class repos_remove_app_access_restrictions_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    branch: Optional[str] = None
    apps: Optional[Any] = None

class repos_get_teams_with_access_to_protected_branch_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    branch: Optional[str] = None

class repos_add_team_access_restrictions_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    branch: Optional[str] = None

class repos_set_team_access_restrictions_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    branch: Optional[str] = None

class repos_remove_team_access_restrictions_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    branch: Optional[str] = None

class repos_get_users_with_access_to_protected_branch_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    branch: Optional[str] = None

class repos_add_user_access_restrictions_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    branch: Optional[str] = None
    users: Optional[Any] = None

class repos_set_user_access_restrictions_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    branch: Optional[str] = None
    users: Optional[Any] = None

class repos_remove_user_access_restrictions_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    branch: Optional[str] = None
    users: Optional[Any] = None

class repos_rename_branch_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    branch: Optional[str] = None
    new_name: Optional[Any] = None

class checks_create_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    name: Optional[Any] = None
    head_sha: Optional[Any] = None
    details_url: Optional[Any] = None
    external_id: Optional[Any] = None
    status: Optional[Any] = None
    started_at: Optional[Any] = None
    conclusion: Optional[Any] = None
    completed_at: Optional[Any] = None
    output: Optional[Any] = None
    actions: Optional[Any] = None

class checks_get_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    check_run_id: Optional[int] = None

class checks_update_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    check_run_id: Optional[int] = None
    name: Optional[Any] = None
    details_url: Optional[Any] = None
    external_id: Optional[Any] = None
    started_at: Optional[Any] = None
    status: Optional[Any] = None
    conclusion: Optional[Any] = None
    completed_at: Optional[Any] = None
    output: Optional[Any] = None
    actions: Optional[Any] = None

class checks_list_annotations_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    check_run_id: Optional[int] = None
    per_page: Optional[int] = None
    page: Optional[int] = None

class checks_rerequest_run_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    check_run_id: Optional[int] = None

class checks_create_suite_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    head_sha: Optional[Any] = None

class checks_set_suites_preferences_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    auto_trigger_checks: Optional[Any] = None

class checks_get_suite_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    check_suite_id: Optional[int] = None

class checks_list_for_suite_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    check_suite_id: Optional[int] = None
    check_name: Optional[str] = None
    status: Optional[str] = None
    filter: Optional[str] = None
    per_page: Optional[int] = None
    page: Optional[int] = None

class checks_rerequest_suite_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    check_suite_id: Optional[int] = None

class code_scanning_list_alerts_for_repo_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    tool_name: Optional[Any] = None
    tool_guid: Optional[Any] = None
    page: Optional[int] = None
    per_page: Optional[int] = None
    ref: Optional[Any] = None
    pr: Optional[int] = None
    direction: Optional[str] = None
    before: Optional[str] = None
    after: Optional[str] = None
    sort: Optional[str] = None
    state: Optional[Any] = None
    severity: Optional[Any] = None

class code_scanning_get_alert_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    alert_number: Optional[Any] = None

class code_scanning_update_alert_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    alert_number: Optional[Any] = None
    state: Optional[Any] = None
    dismissed_reason: Optional[Any] = None
    dismissed_comment: Optional[Any] = None
    create_request: Optional[Any] = None

class code_scanning_get_autofix_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    alert_number: Optional[Any] = None

class code_scanning_create_autofix_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    alert_number: Optional[Any] = None

class code_scanning_commit_autofix_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    alert_number: Optional[Any] = None
    target_ref: Optional[Any] = None
    message: Optional[Any] = None

class code_scanning_list_alert_instances_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    alert_number: Optional[Any] = None
    page: Optional[int] = None
    per_page: Optional[int] = None
    ref: Optional[Any] = None
    pr: Optional[int] = None

class code_scanning_list_recent_analyses_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    tool_name: Optional[Any] = None
    tool_guid: Optional[Any] = None
    page: Optional[int] = None
    per_page: Optional[int] = None
    pr: Optional[int] = None
    ref: Optional[Any] = None
    sarif_id: Optional[Any] = None
    direction: Optional[str] = None
    sort: Optional[str] = None

class code_scanning_get_analysis_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    analysis_id: Optional[int] = None

class code_scanning_delete_analysis_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    analysis_id: Optional[int] = None
    confirm_delete: Optional[str] = None

class code_scanning_list_codeql_databases_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None

class code_scanning_get_codeql_database_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    language: Optional[str] = None

class code_scanning_delete_codeql_database_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    language: Optional[str] = None

class code_scanning_create_variant_analysis_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    language: Optional[Any] = None
    query_pack: Optional[Any] = None
    repositories: Optional[Any] = None
    repository_lists: Optional[Any] = None
    repository_owners: Optional[Any] = None

class code_scanning_get_variant_analysis_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    codeql_variant_analysis_id: Optional[int] = None

class code_scanning_get_variant_analysis_repo_task_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    codeql_variant_analysis_id: Optional[int] = None
    repo_owner: Optional[str] = None
    repo_name: Optional[str] = None

class code_scanning_get_default_setup_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None

class code_scanning_update_default_setup_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    state: Optional[Any] = None
    runner_type: Optional[Any] = None
    runner_label: Optional[Any] = None
    query_suite: Optional[Any] = None
    threat_model: Optional[Any] = None
    languages: Optional[Any] = None

class code_scanning_upload_sarif_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    commit_sha: Optional[Any] = None
    ref: Optional[Any] = None
    sarif: Optional[Any] = None
    checkout_uri: Optional[Any] = None
    started_at: Optional[Any] = None
    tool_name: Optional[Any] = None
    validate: Optional[Any] = None

class code_scanning_get_sarif_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    sarif_id: Optional[str] = None

class code_security_get_configuration_for_repository_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None

class repos_codeowners_errors_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    ref: Optional[str] = None

class codespaces_list_in_repository_for_authenticated_user_params(msgspec.Struct):
    per_page: Optional[int] = None
    page: Optional[int] = None
    owner: Optional[str] = None
    repo: Optional[str] = None

class codespaces_create_with_repo_for_authenticated_user_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    ref: Optional[Any] = None
    location: Optional[Any] = None
    geo: Optional[Any] = None
    client_ip: Optional[Any] = None
    machine: Optional[Any] = None
    devcontainer_path: Optional[Any] = None
    multi_repo_permissions_opt_out: Optional[Any] = None
    working_directory: Optional[Any] = None
    idle_timeout_minutes: Optional[Any] = None
    display_name: Optional[Any] = None
    retention_period_minutes: Optional[Any] = None

class codespaces_list_devcontainers_in_repository_for_authenticated_user_params(msgspec.Struct):
    per_page: Optional[int] = None
    page: Optional[int] = None
    owner: Optional[str] = None
    repo: Optional[str] = None

class codespaces_repo_machines_for_authenticated_user_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    location: Optional[str] = None
    client_ip: Optional[str] = None
    ref: Optional[str] = None

class codespaces_pre_flight_with_repo_for_authenticated_user_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    ref: Optional[str] = None
    client_ip: Optional[str] = None

class codespaces_check_permissions_for_devcontainer_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    ref: Optional[str] = None
    devcontainer_path: Optional[str] = None

class codespaces_list_repo_secrets_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    per_page: Optional[int] = None
    page: Optional[int] = None

class codespaces_get_repo_public_key_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None

class codespaces_get_repo_secret_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    secret_name: Optional[str] = None

class codespaces_create_or_update_repo_secret_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    secret_name: Optional[str] = None
    encrypted_value: Optional[Any] = None
    key_id: Optional[Any] = None

class codespaces_delete_repo_secret_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    secret_name: Optional[str] = None

class repos_list_collaborators_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    affiliation: Optional[str] = None
    permission: Optional[str] = None
    per_page: Optional[int] = None
    page: Optional[int] = None

class repos_check_collaborator_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    username: Optional[str] = None

class repos_add_collaborator_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    username: Optional[str] = None
    permission: Optional[Any] = None

class repos_remove_collaborator_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    username: Optional[str] = None

class repos_get_collaborator_permission_level_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    username: Optional[str] = None

class repos_list_commit_comments_for_repo_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    per_page: Optional[int] = None
    page: Optional[int] = None

class repos_get_commit_comment_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    comment_id: Optional[int] = None

class repos_update_commit_comment_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    comment_id: Optional[int] = None
    body: Optional[Any] = None

class repos_delete_commit_comment_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    comment_id: Optional[int] = None

class reactions_list_for_commit_comment_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    comment_id: Optional[int] = None
    content: Optional[str] = None
    per_page: Optional[int] = None
    page: Optional[int] = None

class reactions_create_for_commit_comment_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    comment_id: Optional[int] = None
    content: Optional[Any] = None

class reactions_delete_for_commit_comment_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    comment_id: Optional[int] = None
    reaction_id: Optional[int] = None

class repos_list_commits_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    sha: Optional[str] = None
    path: Optional[str] = None
    author: Optional[str] = None
    committer: Optional[str] = None
    since: Optional[str] = None
    until: Optional[str] = None
    per_page: Optional[int] = None
    page: Optional[int] = None

class repos_list_branches_for_head_commit_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    commit_sha: Optional[str] = None

class repos_list_comments_for_commit_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    commit_sha: Optional[str] = None
    per_page: Optional[int] = None
    page: Optional[int] = None

class repos_create_commit_comment_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    commit_sha: Optional[str] = None
    body: Optional[Any] = None
    path: Optional[Any] = None
    position: Optional[Any] = None
    line: Optional[Any] = None

class repos_list_pull_requests_associated_with_commit_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    commit_sha: Optional[str] = None
    per_page: Optional[int] = None
    page: Optional[int] = None

class repos_get_commit_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    page: Optional[int] = None
    per_page: Optional[int] = None
    ref: Optional[str] = None

class checks_list_for_ref_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    ref: Optional[str] = None
    check_name: Optional[str] = None
    status: Optional[str] = None
    filter: Optional[str] = None
    per_page: Optional[int] = None
    page: Optional[int] = None
    app_id: Optional[int] = None

class checks_list_suites_for_ref_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    ref: Optional[str] = None
    app_id: Optional[int] = None
    check_name: Optional[str] = None
    per_page: Optional[int] = None
    page: Optional[int] = None

class repos_get_combined_status_for_ref_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    ref: Optional[str] = None
    per_page: Optional[int] = None
    page: Optional[int] = None

class repos_list_commit_statuses_for_ref_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    ref: Optional[str] = None
    per_page: Optional[int] = None
    page: Optional[int] = None

class repos_get_community_profile_metrics_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None

class repos_compare_commits_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    page: Optional[int] = None
    per_page: Optional[int] = None
    basehead: Optional[str] = None

class repos_get_content_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    path: Optional[str] = None
    ref: Optional[str] = None

class repos_create_or_update_file_contents_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    path: Optional[str] = None
    message: Optional[Any] = None
    content: Optional[Any] = None
    sha: Optional[Any] = None
    branch: Optional[Any] = None
    committer: Optional[Any] = None
    author: Optional[Any] = None

class repos_delete_file_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    path: Optional[str] = None
    message: Optional[Any] = None
    sha: Optional[Any] = None
    branch: Optional[Any] = None
    committer: Optional[Any] = None
    author: Optional[Any] = None

class repos_list_contributors_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    anon: Optional[str] = None
    per_page: Optional[int] = None
    page: Optional[int] = None

class dependabot_list_alerts_for_repo_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    state: Optional[str] = None
    severity: Optional[str] = None
    ecosystem: Optional[str] = None
    package: Optional[str] = None
    manifest: Optional[str] = None
    epss_percentage: Optional[str] = None
    has: Optional[Any] = None
    scope: Optional[str] = None
    sort: Optional[str] = None
    direction: Optional[str] = None
    page: Optional[int] = None
    per_page: Optional[int] = None
    before: Optional[str] = None
    after: Optional[str] = None
    first: Optional[int] = None
    last: Optional[int] = None

class dependabot_get_alert_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    alert_number: Optional[Any] = None

class dependabot_update_alert_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    alert_number: Optional[Any] = None
    state: Optional[Any] = None
    dismissed_reason: Optional[Any] = None
    dismissed_comment: Optional[Any] = None

class dependabot_list_repo_secrets_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    per_page: Optional[int] = None
    page: Optional[int] = None

class dependabot_get_repo_public_key_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None

class dependabot_get_repo_secret_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    secret_name: Optional[str] = None

class dependabot_create_or_update_repo_secret_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    secret_name: Optional[str] = None
    encrypted_value: Optional[Any] = None
    key_id: Optional[Any] = None

class dependabot_delete_repo_secret_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    secret_name: Optional[str] = None

class dependency_graph_diff_range_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    basehead: Optional[str] = None
    name: Optional[str] = None

class dependency_graph_export_sbom_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None

class dependency_graph_create_repository_snapshot_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    version: Optional[Any] = None
    job: Optional[Any] = None
    sha: Optional[Any] = None
    ref: Optional[Any] = None
    detector: Optional[Any] = None
    metadata: Optional[Any] = None
    manifests: Optional[Any] = None
    scanned: Optional[Any] = None

class repos_list_deployments_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    sha: Optional[str] = None
    ref: Optional[str] = None
    task: Optional[str] = None
    environment: Optional[str] = None
    per_page: Optional[int] = None
    page: Optional[int] = None

class repos_create_deployment_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    ref: Optional[Any] = None
    task: Optional[Any] = None
    auto_merge: Optional[Any] = None
    required_contexts: Optional[Any] = None
    payload: Optional[Any] = None
    environment: Optional[Any] = None
    description: Optional[Any] = None
    transient_environment: Optional[Any] = None
    production_environment: Optional[Any] = None

class repos_get_deployment_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    deployment_id: Optional[int] = None

class repos_delete_deployment_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    deployment_id: Optional[int] = None

class repos_list_deployment_statuses_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    deployment_id: Optional[int] = None
    per_page: Optional[int] = None
    page: Optional[int] = None

class repos_create_deployment_status_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    deployment_id: Optional[int] = None
    state: Optional[Any] = None
    target_url: Optional[Any] = None
    log_url: Optional[Any] = None
    description: Optional[Any] = None
    environment: Optional[Any] = None
    environment_url: Optional[Any] = None
    auto_inactive: Optional[Any] = None

class repos_get_deployment_status_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    deployment_id: Optional[int] = None
    status_id: Optional[int] = None

class repos_create_dispatch_event_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    event_type: Optional[Any] = None
    client_payload: Optional[Any] = None

class repos_get_all_environments_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    per_page: Optional[int] = None
    page: Optional[int] = None

class repos_get_environment_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    environment_name: Optional[str] = None

class repos_create_or_update_environment_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    environment_name: Optional[str] = None
    wait_timer: Optional[Any] = None
    prevent_self_review: Optional[Any] = None
    reviewers: Optional[Any] = None
    deployment_branch_policy: Optional[Any] = None

class repos_delete_an_environment_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    environment_name: Optional[str] = None

class repos_list_deployment_branch_policies_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    environment_name: Optional[str] = None
    per_page: Optional[int] = None
    page: Optional[int] = None

class repos_create_deployment_branch_policy_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    environment_name: Optional[str] = None
    name: Optional[Any] = None
    type: Optional[Any] = None

class repos_get_deployment_branch_policy_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    environment_name: Optional[str] = None
    branch_policy_id: Optional[int] = None

class repos_update_deployment_branch_policy_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    environment_name: Optional[str] = None
    branch_policy_id: Optional[int] = None
    name: Optional[Any] = None

class repos_delete_deployment_branch_policy_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    environment_name: Optional[str] = None
    branch_policy_id: Optional[int] = None

class repos_get_all_deployment_protection_rules_params(msgspec.Struct):
    environment_name: Optional[str] = None
    repo: Optional[str] = None
    owner: Optional[str] = None

class repos_create_deployment_protection_rule_params(msgspec.Struct):
    environment_name: Optional[str] = None
    repo: Optional[str] = None
    owner: Optional[str] = None
    integration_id: Optional[Any] = None

class repos_list_custom_deployment_rule_integrations_params(msgspec.Struct):
    environment_name: Optional[str] = None
    repo: Optional[str] = None
    owner: Optional[str] = None
    page: Optional[int] = None
    per_page: Optional[int] = None

class repos_get_custom_deployment_protection_rule_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    environment_name: Optional[str] = None
    protection_rule_id: Optional[int] = None

class repos_disable_deployment_protection_rule_params(msgspec.Struct):
    environment_name: Optional[str] = None
    repo: Optional[str] = None
    owner: Optional[str] = None
    protection_rule_id: Optional[int] = None

class actions_list_environment_secrets_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    environment_name: Optional[str] = None
    per_page: Optional[int] = None
    page: Optional[int] = None

class actions_get_environment_public_key_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    environment_name: Optional[str] = None

class actions_get_environment_secret_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    environment_name: Optional[str] = None
    secret_name: Optional[str] = None

class actions_create_or_update_environment_secret_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    environment_name: Optional[str] = None
    secret_name: Optional[str] = None
    encrypted_value: Optional[Any] = None
    key_id: Optional[Any] = None

class actions_delete_environment_secret_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    environment_name: Optional[str] = None
    secret_name: Optional[str] = None

class actions_list_environment_variables_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    environment_name: Optional[str] = None
    per_page: Optional[int] = None
    page: Optional[int] = None

class actions_create_environment_variable_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    environment_name: Optional[str] = None
    name: Optional[Any] = None
    value: Optional[Any] = None

class actions_get_environment_variable_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    environment_name: Optional[str] = None
    name: Optional[str] = None

class actions_update_environment_variable_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    name: Optional[str] = None
    environment_name: Optional[str] = None
    name_: Optional[Any] = None
    value: Optional[Any] = None

class actions_delete_environment_variable_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    name: Optional[str] = None
    environment_name: Optional[str] = None

class activity_list_repo_events_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    per_page: Optional[int] = None
    page: Optional[int] = None

class repos_list_forks_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    sort: Optional[str] = None
    per_page: Optional[int] = None
    page: Optional[int] = None

class repos_create_fork_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    organization: Optional[Any] = None
    name: Optional[Any] = None
    default_branch_only: Optional[Any] = None

class git_create_blob_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    content: Optional[Any] = None
    encoding: Optional[Any] = None

class git_get_blob_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    file_sha: Optional[str] = None

class git_create_commit_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    message: Optional[Any] = None
    tree: Optional[Any] = None
    parents: Optional[Any] = None
    author: Optional[Any] = None
    committer: Optional[Any] = None
    signature: Optional[Any] = None

class git_get_commit_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    commit_sha: Optional[str] = None

class git_list_matching_refs_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    ref: Optional[str] = None

class git_get_ref_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    ref: Optional[str] = None

class git_create_ref_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    ref: Optional[Any] = None
    sha: Optional[Any] = None

class git_update_ref_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    ref: Optional[str] = None
    sha: Optional[Any] = None
    force: Optional[Any] = None

class git_delete_ref_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    ref: Optional[str] = None

class git_create_tag_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    tag: Optional[Any] = None
    message: Optional[Any] = None
    object: Optional[Any] = None
    type: Optional[Any] = None
    tagger: Optional[Any] = None

class git_get_tag_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    tag_sha: Optional[str] = None

class git_create_tree_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    tree: Optional[Any] = None
    base_tree: Optional[Any] = None

class git_get_tree_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    tree_sha: Optional[str] = None
    recursive: Optional[str] = None

class repos_list_webhooks_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    per_page: Optional[int] = None
    page: Optional[int] = None

class repos_create_webhook_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    name: Optional[Any] = None
    config: Optional[Any] = None
    events: Optional[Any] = None
    active: Optional[Any] = None

class repos_get_webhook_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    hook_id: Optional[int] = None

class repos_update_webhook_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    hook_id: Optional[int] = None
    config: Optional[Any] = None
    events: Optional[Any] = None
    add_events: Optional[Any] = None
    remove_events: Optional[Any] = None
    active: Optional[Any] = None

class repos_delete_webhook_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    hook_id: Optional[int] = None

class repos_get_webhook_config_for_repo_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    hook_id: Optional[int] = None

class repos_update_webhook_config_for_repo_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    hook_id: Optional[int] = None
    url: Optional[Any] = None
    content_type: Optional[Any] = None
    secret: Optional[Any] = None
    insecure_ssl: Optional[Any] = None

class repos_list_webhook_deliveries_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    hook_id: Optional[int] = None
    per_page: Optional[int] = None
    cursor: Optional[str] = None

class repos_get_webhook_delivery_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    hook_id: Optional[int] = None
    delivery_id: Optional[int] = None

class repos_redeliver_webhook_delivery_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    hook_id: Optional[int] = None
    delivery_id: Optional[int] = None

class repos_ping_webhook_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    hook_id: Optional[int] = None

class repos_test_push_webhook_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    hook_id: Optional[int] = None

class migrations_get_import_status_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None

class migrations_start_import_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    vcs_url: Optional[Any] = None
    vcs: Optional[Any] = None
    vcs_username: Optional[Any] = None
    vcs_password: Optional[Any] = None
    tfvc_project: Optional[Any] = None

class migrations_update_import_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    vcs_username: Optional[Any] = None
    vcs_password: Optional[Any] = None
    vcs: Optional[Any] = None
    tfvc_project: Optional[Any] = None

class migrations_cancel_import_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None

class migrations_get_commit_authors_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    since: Optional[int] = None

class migrations_map_commit_author_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    author_id: Optional[int] = None
    email: Optional[Any] = None
    name: Optional[Any] = None

class migrations_get_large_files_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None

class migrations_set_lfs_preference_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    use_lfs: Optional[Any] = None

class apps_get_repo_installation_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None

class interactions_get_restrictions_for_repo_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None

class interactions_set_restrictions_for_repo_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    limit: Optional[Any] = None
    expiry: Optional[Any] = None

class interactions_remove_restrictions_for_repo_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None

class repos_list_invitations_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    per_page: Optional[int] = None
    page: Optional[int] = None

class repos_update_invitation_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    invitation_id: Optional[int] = None
    permissions: Optional[Any] = None

class repos_delete_invitation_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    invitation_id: Optional[int] = None

class issues_list_for_repo_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    milestone: Optional[str] = None
    state: Optional[str] = None
    assignee: Optional[str] = None
    type: Optional[str] = None
    creator: Optional[str] = None
    mentioned: Optional[str] = None
    labels: Optional[str] = None
    sort: Optional[str] = None
    direction: Optional[str] = None
    since: Optional[str] = None
    per_page: Optional[int] = None
    page: Optional[int] = None

class issues_create_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    title: Optional[Any] = None
    body: Optional[Any] = None
    assignee: Optional[Any] = None
    milestone: Optional[Any] = None
    labels: Optional[Any] = None
    assignees: Optional[Any] = None
    type: Optional[Any] = None

class issues_list_comments_for_repo_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    sort: Optional[str] = None
    direction: Optional[str] = None
    since: Optional[str] = None
    per_page: Optional[int] = None
    page: Optional[int] = None

class issues_get_comment_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    comment_id: Optional[int] = None

class issues_update_comment_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    comment_id: Optional[int] = None
    body: Optional[Any] = None

class issues_delete_comment_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    comment_id: Optional[int] = None

class reactions_list_for_issue_comment_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    comment_id: Optional[int] = None
    content: Optional[str] = None
    per_page: Optional[int] = None
    page: Optional[int] = None

class reactions_create_for_issue_comment_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    comment_id: Optional[int] = None
    content: Optional[Any] = None

class reactions_delete_for_issue_comment_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    comment_id: Optional[int] = None
    reaction_id: Optional[int] = None

class issues_list_events_for_repo_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    per_page: Optional[int] = None
    page: Optional[int] = None

class issues_get_event_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    event_id: Optional[int] = None

class issues_get_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    issue_number: Optional[int] = None

class issues_update_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    issue_number: Optional[int] = None
    title: Optional[Any] = None
    body: Optional[Any] = None
    assignee: Optional[Any] = None
    state: Optional[Any] = None
    state_reason: Optional[Any] = None
    milestone: Optional[Any] = None
    labels: Optional[Any] = None
    assignees: Optional[Any] = None
    type: Optional[Any] = None

class issues_add_assignees_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    issue_number: Optional[int] = None
    assignees: Optional[Any] = None

class issues_remove_assignees_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    issue_number: Optional[int] = None
    assignees: Optional[Any] = None

class issues_check_user_can_be_assigned_to_issue_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    issue_number: Optional[int] = None
    assignee: Optional[str] = None

class issues_list_comments_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    issue_number: Optional[int] = None
    since: Optional[str] = None
    per_page: Optional[int] = None
    page: Optional[int] = None

class issues_create_comment_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    issue_number: Optional[int] = None
    body: Optional[Any] = None

class issues_list_dependencies_blocked_by_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    issue_number: Optional[int] = None
    per_page: Optional[int] = None
    page: Optional[int] = None

class issues_add_blocked_by_dependency_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    issue_number: Optional[int] = None
    issue_id: Optional[Any] = None

class issues_remove_dependency_blocked_by_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    issue_number: Optional[int] = None
    issue_id: Optional[int] = None

class issues_list_dependencies_blocking_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    issue_number: Optional[int] = None
    per_page: Optional[int] = None
    page: Optional[int] = None

class issues_list_events_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    issue_number: Optional[int] = None
    per_page: Optional[int] = None
    page: Optional[int] = None

class issues_list_labels_on_issue_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    issue_number: Optional[int] = None
    per_page: Optional[int] = None
    page: Optional[int] = None

class issues_add_labels_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    issue_number: Optional[int] = None

class issues_set_labels_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    issue_number: Optional[int] = None

class issues_remove_all_labels_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    issue_number: Optional[int] = None

class issues_remove_label_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    issue_number: Optional[int] = None
    name: Optional[str] = None

class issues_lock_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    issue_number: Optional[int] = None
    lock_reason: Optional[Any] = None

class issues_unlock_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    issue_number: Optional[int] = None

class issues_get_parent_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    issue_number: Optional[int] = None

class reactions_list_for_issue_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    issue_number: Optional[int] = None
    content: Optional[str] = None
    per_page: Optional[int] = None
    page: Optional[int] = None

class reactions_create_for_issue_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    issue_number: Optional[int] = None
    content: Optional[Any] = None

class reactions_delete_for_issue_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    issue_number: Optional[int] = None
    reaction_id: Optional[int] = None

class issues_remove_sub_issue_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    issue_number: Optional[int] = None
    sub_issue_id: Optional[Any] = None

class issues_list_sub_issues_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    issue_number: Optional[int] = None
    per_page: Optional[int] = None
    page: Optional[int] = None

class issues_add_sub_issue_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    issue_number: Optional[int] = None
    sub_issue_id: Optional[Any] = None
    replace_parent: Optional[Any] = None

class issues_reprioritize_sub_issue_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    issue_number: Optional[int] = None
    sub_issue_id: Optional[Any] = None
    after_id: Optional[Any] = None
    before_id: Optional[Any] = None

class issues_list_events_for_timeline_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    issue_number: Optional[int] = None
    per_page: Optional[int] = None
    page: Optional[int] = None

class repos_list_deploy_keys_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    per_page: Optional[int] = None
    page: Optional[int] = None

class repos_create_deploy_key_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    title: Optional[Any] = None
    key: Optional[Any] = None
    read_only: Optional[Any] = None

class repos_get_deploy_key_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    key_id: Optional[int] = None

class repos_delete_deploy_key_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    key_id: Optional[int] = None

class issues_list_labels_for_repo_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    per_page: Optional[int] = None
    page: Optional[int] = None

class issues_create_label_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    name: Optional[Any] = None
    color: Optional[Any] = None
    description: Optional[Any] = None

class issues_get_label_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    name: Optional[str] = None

class issues_update_label_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    name: Optional[str] = None
    new_name: Optional[Any] = None
    color: Optional[Any] = None
    description: Optional[Any] = None

class issues_delete_label_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    name: Optional[str] = None

class repos_list_languages_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None

class licenses_get_for_repo_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    ref: Optional[Any] = None

class repos_merge_upstream_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    branch: Optional[Any] = None

class repos_merge_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    base: Optional[Any] = None
    head: Optional[Any] = None
    commit_message: Optional[Any] = None

class issues_list_milestones_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    state: Optional[str] = None
    sort: Optional[str] = None
    direction: Optional[str] = None
    per_page: Optional[int] = None
    page: Optional[int] = None

class issues_create_milestone_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    title: Optional[Any] = None
    state: Optional[Any] = None
    description: Optional[Any] = None
    due_on: Optional[Any] = None

class issues_get_milestone_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    milestone_number: Optional[int] = None

class issues_update_milestone_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    milestone_number: Optional[int] = None
    title: Optional[Any] = None
    state: Optional[Any] = None
    description: Optional[Any] = None
    due_on: Optional[Any] = None

class issues_delete_milestone_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    milestone_number: Optional[int] = None

class issues_list_labels_for_milestone_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    milestone_number: Optional[int] = None
    per_page: Optional[int] = None
    page: Optional[int] = None

class activity_list_repo_notifications_for_authenticated_user_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    all: Optional[bool] = None
    participating: Optional[bool] = None
    since: Optional[str] = None
    before: Optional[str] = None
    per_page: Optional[int] = None
    page: Optional[int] = None

class activity_mark_repo_notifications_as_read_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    last_read_at: Optional[Any] = None

class repos_get_pages_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None

class repos_create_pages_site_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    build_type: Optional[Any] = None
    source: Optional[Any] = None

class repos_update_information_about_pages_site_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    cname: Optional[Any] = None
    https_enforced: Optional[Any] = None
    build_type: Optional[Any] = None
    source: Optional[Any] = None

class repos_delete_pages_site_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None

class repos_list_pages_builds_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    per_page: Optional[int] = None
    page: Optional[int] = None

class repos_request_pages_build_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None

class repos_get_latest_pages_build_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None

class repos_get_pages_build_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    build_id: Optional[int] = None

class repos_create_pages_deployment_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    artifact_id: Optional[Any] = None
    artifact_url: Optional[Any] = None
    environment: Optional[Any] = None
    pages_build_version: Optional[Any] = None
    oidc_token: Optional[Any] = None

class repos_get_pages_deployment_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    pages_deployment_id: Optional[Any] = None

class repos_cancel_pages_deployment_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    pages_deployment_id: Optional[Any] = None

class repos_get_pages_health_check_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None

class repos_check_private_vulnerability_reporting_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None

class repos_enable_private_vulnerability_reporting_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None

class repos_disable_private_vulnerability_reporting_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None

class projects_classic_list_for_repo_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    state: Optional[str] = None
    per_page: Optional[int] = None
    page: Optional[int] = None

class projects_classic_create_for_repo_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    name: Optional[Any] = None
    body: Optional[Any] = None

class repos_get_custom_properties_values_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None

class repos_create_or_update_custom_properties_values_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    properties: Optional[Any] = None

class pulls_list_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    state: Optional[str] = None
    head: Optional[str] = None
    base: Optional[str] = None
    sort: Optional[str] = None
    direction: Optional[str] = None
    per_page: Optional[int] = None
    page: Optional[int] = None

class pulls_create_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    title: Optional[Any] = None
    head: Optional[Any] = None
    head_repo: Optional[Any] = None
    base: Optional[Any] = None
    body: Optional[Any] = None
    maintainer_can_modify: Optional[Any] = None
    draft: Optional[Any] = None
    issue: Optional[Any] = None

class pulls_list_review_comments_for_repo_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    sort: Optional[str] = None
    direction: Optional[str] = None
    since: Optional[str] = None
    per_page: Optional[int] = None
    page: Optional[int] = None

class pulls_get_review_comment_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    comment_id: Optional[int] = None

class pulls_update_review_comment_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    comment_id: Optional[int] = None
    body: Optional[Any] = None

class pulls_delete_review_comment_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    comment_id: Optional[int] = None

class reactions_list_for_pull_request_review_comment_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    comment_id: Optional[int] = None
    content: Optional[str] = None
    per_page: Optional[int] = None
    page: Optional[int] = None

class reactions_create_for_pull_request_review_comment_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    comment_id: Optional[int] = None
    content: Optional[Any] = None

class reactions_delete_for_pull_request_comment_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    comment_id: Optional[int] = None
    reaction_id: Optional[int] = None

class pulls_get_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    pull_number: Optional[int] = None

class pulls_update_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    pull_number: Optional[int] = None
    title: Optional[Any] = None
    body: Optional[Any] = None
    state: Optional[Any] = None
    base: Optional[Any] = None
    maintainer_can_modify: Optional[Any] = None

class codespaces_create_with_pr_for_authenticated_user_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    pull_number: Optional[int] = None
    location: Optional[Any] = None
    geo: Optional[Any] = None
    client_ip: Optional[Any] = None
    machine: Optional[Any] = None
    devcontainer_path: Optional[Any] = None
    multi_repo_permissions_opt_out: Optional[Any] = None
    working_directory: Optional[Any] = None
    idle_timeout_minutes: Optional[Any] = None
    display_name: Optional[Any] = None
    retention_period_minutes: Optional[Any] = None

class pulls_list_review_comments_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    pull_number: Optional[int] = None
    sort: Optional[str] = None
    direction: Optional[str] = None
    since: Optional[str] = None
    per_page: Optional[int] = None
    page: Optional[int] = None

class pulls_create_review_comment_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    pull_number: Optional[int] = None
    body: Optional[Any] = None
    commit_id: Optional[Any] = None
    path: Optional[Any] = None
    position: Optional[Any] = None
    side: Optional[Any] = None
    line: Optional[Any] = None
    start_line: Optional[Any] = None
    start_side: Optional[Any] = None
    in_reply_to: Optional[Any] = None
    subject_type: Optional[Any] = None

class pulls_create_reply_for_review_comment_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    pull_number: Optional[int] = None
    comment_id: Optional[int] = None
    body: Optional[Any] = None

class pulls_list_commits_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    pull_number: Optional[int] = None
    per_page: Optional[int] = None
    page: Optional[int] = None

class pulls_list_files_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    pull_number: Optional[int] = None
    per_page: Optional[int] = None
    page: Optional[int] = None

class pulls_check_if_merged_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    pull_number: Optional[int] = None

class pulls_merge_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    pull_number: Optional[int] = None
    commit_title: Optional[Any] = None
    commit_message: Optional[Any] = None
    sha: Optional[Any] = None
    merge_method: Optional[Any] = None

class pulls_list_requested_reviewers_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    pull_number: Optional[int] = None

class pulls_request_reviewers_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    pull_number: Optional[int] = None
    reviewers: Optional[Any] = None
    team_reviewers: Optional[Any] = None

class pulls_remove_requested_reviewers_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    pull_number: Optional[int] = None
    reviewers: Optional[Any] = None
    team_reviewers: Optional[Any] = None

class pulls_list_reviews_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    pull_number: Optional[int] = None
    per_page: Optional[int] = None
    page: Optional[int] = None

class pulls_create_review_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    pull_number: Optional[int] = None
    commit_id: Optional[Any] = None
    body: Optional[Any] = None
    event: Optional[Any] = None
    comments: Optional[Any] = None

class pulls_get_review_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    pull_number: Optional[int] = None
    review_id: Optional[int] = None

class pulls_update_review_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    pull_number: Optional[int] = None
    review_id: Optional[int] = None
    body: Optional[Any] = None

class pulls_delete_pending_review_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    pull_number: Optional[int] = None
    review_id: Optional[int] = None

class pulls_list_comments_for_review_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    pull_number: Optional[int] = None
    review_id: Optional[int] = None
    per_page: Optional[int] = None
    page: Optional[int] = None

class pulls_dismiss_review_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    pull_number: Optional[int] = None
    review_id: Optional[int] = None
    message: Optional[Any] = None
    event: Optional[Any] = None

class pulls_submit_review_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    pull_number: Optional[int] = None
    review_id: Optional[int] = None
    body: Optional[Any] = None
    event: Optional[Any] = None

class pulls_update_branch_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    pull_number: Optional[int] = None
    expected_head_sha: Optional[Any] = None

class repos_get_readme_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    ref: Optional[str] = None

class repos_get_readme_in_directory_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    dir: Optional[str] = None
    ref: Optional[str] = None

class repos_list_releases_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    per_page: Optional[int] = None
    page: Optional[int] = None

class repos_create_release_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    tag_name: Optional[Any] = None
    target_commitish: Optional[Any] = None
    name: Optional[Any] = None
    body: Optional[Any] = None
    draft: Optional[Any] = None
    prerelease: Optional[Any] = None
    discussion_category_name: Optional[Any] = None
    generate_release_notes: Optional[Any] = None
    make_latest: Optional[Any] = None

class repos_get_release_asset_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    asset_id: Optional[int] = None

class repos_update_release_asset_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    asset_id: Optional[int] = None
    name: Optional[Any] = None
    label: Optional[Any] = None
    state: Optional[Any] = None

class repos_delete_release_asset_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    asset_id: Optional[int] = None

class repos_generate_release_notes_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    tag_name: Optional[Any] = None
    target_commitish: Optional[Any] = None
    previous_tag_name: Optional[Any] = None
    configuration_file_path: Optional[Any] = None

class repos_get_latest_release_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None

class repos_get_release_by_tag_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    tag: Optional[str] = None

class repos_get_release_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    release_id: Optional[int] = None

class repos_update_release_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    release_id: Optional[int] = None
    tag_name: Optional[Any] = None
    target_commitish: Optional[Any] = None
    name: Optional[Any] = None
    body: Optional[Any] = None
    draft: Optional[Any] = None
    prerelease: Optional[Any] = None
    make_latest: Optional[Any] = None
    discussion_category_name: Optional[Any] = None

class repos_delete_release_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    release_id: Optional[int] = None

class repos_list_release_assets_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    release_id: Optional[int] = None
    per_page: Optional[int] = None
    page: Optional[int] = None

class repos_upload_release_asset_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    release_id: Optional[int] = None
    name: Optional[str] = None
    label: Optional[str] = None

class reactions_list_for_release_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    release_id: Optional[int] = None
    content: Optional[str] = None
    per_page: Optional[int] = None
    page: Optional[int] = None

class reactions_create_for_release_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    release_id: Optional[int] = None
    content: Optional[Any] = None

class reactions_delete_for_release_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    release_id: Optional[int] = None
    reaction_id: Optional[int] = None

class repos_get_branch_rules_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    branch: Optional[str] = None
    per_page: Optional[int] = None
    page: Optional[int] = None

class repos_get_repo_rulesets_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    per_page: Optional[int] = None
    page: Optional[int] = None
    includes_parents: Optional[bool] = None
    targets: Optional[str] = None

class repos_create_repo_ruleset_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    name: Optional[Any] = None
    target: Optional[Any] = None
    enforcement: Optional[Any] = None
    bypass_actors: Optional[Any] = None
    conditions: Optional[Any] = None
    rules: Optional[Any] = None

class repos_get_repo_rule_suites_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    ref: Optional[str] = None
    time_period: Optional[str] = None
    actor_name: Optional[str] = None
    rule_suite_result: Optional[str] = None
    per_page: Optional[int] = None
    page: Optional[int] = None

class repos_get_repo_rule_suite_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    rule_suite_id: Optional[int] = None

class repos_get_repo_ruleset_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    ruleset_id: Optional[int] = None
    includes_parents: Optional[bool] = None

class repos_update_repo_ruleset_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    ruleset_id: Optional[int] = None
    name: Optional[Any] = None
    target: Optional[Any] = None
    enforcement: Optional[Any] = None
    bypass_actors: Optional[Any] = None
    conditions: Optional[Any] = None
    rules: Optional[Any] = None

class repos_delete_repo_ruleset_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    ruleset_id: Optional[int] = None

class repos_get_repo_ruleset_history_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    per_page: Optional[int] = None
    page: Optional[int] = None
    ruleset_id: Optional[int] = None

class repos_get_repo_ruleset_version_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    ruleset_id: Optional[int] = None
    version_id: Optional[int] = None

class secret_scanning_list_alerts_for_repo_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    state: Optional[str] = None
    secret_type: Optional[str] = None
    resolution: Optional[str] = None
    sort: Optional[str] = None
    direction: Optional[str] = None
    page: Optional[int] = None
    per_page: Optional[int] = None
    before: Optional[str] = None
    after: Optional[str] = None
    validity: Optional[str] = None
    is_publicly_leaked: Optional[bool] = None
    is_multi_repo: Optional[bool] = None
    hide_secret: Optional[bool] = None

class secret_scanning_get_alert_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    alert_number: Optional[Any] = None
    hide_secret: Optional[bool] = None

class secret_scanning_update_alert_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    alert_number: Optional[Any] = None
    state: Optional[Any] = None
    resolution: Optional[Any] = None
    resolution_comment: Optional[Any] = None

class secret_scanning_list_locations_for_alert_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    alert_number: Optional[Any] = None
    page: Optional[int] = None
    per_page: Optional[int] = None

class secret_scanning_create_push_protection_bypass_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    reason: Optional[Any] = None
    placeholder_id: Optional[Any] = None

class secret_scanning_get_scan_history_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None

class security_advisories_list_repository_advisories_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    direction: Optional[str] = None
    sort: Optional[str] = None
    before: Optional[str] = None
    after: Optional[str] = None
    per_page: Optional[int] = None
    state: Optional[str] = None

class security_advisories_create_repository_advisory_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    summary: Optional[Any] = None
    description: Optional[Any] = None
    cve_id: Optional[Any] = None
    vulnerabilities: Optional[Any] = None
    cwe_ids: Optional[Any] = None
    credits: Optional[Any] = None
    severity: Optional[Any] = None
    cvss_vector_string: Optional[Any] = None
    start_private_fork: Optional[Any] = None

class security_advisories_create_private_vulnerability_report_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    summary: Optional[Any] = None
    description: Optional[Any] = None
    vulnerabilities: Optional[Any] = None
    cwe_ids: Optional[Any] = None
    severity: Optional[Any] = None
    cvss_vector_string: Optional[Any] = None
    start_private_fork: Optional[Any] = None

class security_advisories_get_repository_advisory_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    ghsa_id: Optional[str] = None

class security_advisories_update_repository_advisory_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    ghsa_id: Optional[str] = None
    summary: Optional[Any] = None
    description: Optional[Any] = None
    cve_id: Optional[Any] = None
    vulnerabilities: Optional[Any] = None
    cwe_ids: Optional[Any] = None
    credits: Optional[Any] = None
    severity: Optional[Any] = None
    cvss_vector_string: Optional[Any] = None
    state: Optional[Any] = None
    collaborating_users: Optional[Any] = None
    collaborating_teams: Optional[Any] = None

class security_advisories_create_repository_advisory_cve_request_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    ghsa_id: Optional[str] = None

class security_advisories_create_fork_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    ghsa_id: Optional[str] = None

class activity_list_stargazers_for_repo_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    per_page: Optional[int] = None
    page: Optional[int] = None

class repos_get_code_frequency_stats_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None

class repos_get_commit_activity_stats_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None

class repos_get_contributors_stats_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None

class repos_get_participation_stats_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None

class repos_get_punch_card_stats_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None

class repos_create_commit_status_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    sha: Optional[str] = None
    state: Optional[Any] = None
    target_url: Optional[Any] = None
    description: Optional[Any] = None
    context: Optional[Any] = None

class activity_list_watchers_for_repo_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    per_page: Optional[int] = None
    page: Optional[int] = None

class activity_get_repo_subscription_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None

class activity_set_repo_subscription_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    subscribed: Optional[Any] = None
    ignored: Optional[Any] = None

class activity_delete_repo_subscription_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None

class repos_list_tags_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    per_page: Optional[int] = None
    page: Optional[int] = None

class repos_list_tag_protection_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None

class repos_create_tag_protection_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    pattern: Optional[Any] = None

class repos_delete_tag_protection_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    tag_protection_id: Optional[int] = None

class repos_download_tarball_archive_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    ref: Optional[str] = None

class repos_list_teams_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    per_page: Optional[int] = None
    page: Optional[int] = None

class repos_get_all_topics_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    page: Optional[int] = None
    per_page: Optional[int] = None

class repos_replace_all_topics_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    names: Optional[Any] = None

class repos_get_clones_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    per: Optional[str] = None

class repos_get_top_paths_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None

class repos_get_top_referrers_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None

class repos_get_views_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    per: Optional[str] = None

class repos_transfer_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    new_owner: Optional[Any] = None
    new_name: Optional[Any] = None
    team_ids: Optional[Any] = None

class repos_check_vulnerability_alerts_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None

class repos_enable_vulnerability_alerts_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None

class repos_disable_vulnerability_alerts_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None

class repos_download_zipball_archive_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None
    ref: Optional[str] = None

class repos_create_using_template_params(msgspec.Struct):
    template_owner: Optional[str] = None
    template_repo: Optional[str] = None
    owner: Optional[Any] = None
    name: Optional[Any] = None
    description: Optional[Any] = None
    include_all_branches: Optional[Any] = None
    private: Optional[Any] = None

class repos_list_public_params(msgspec.Struct):
    since: Optional[int] = None

class search_code_params(msgspec.Struct):
    q: Optional[str] = None
    sort: Optional[str] = None
    order: Optional[str] = None
    per_page: Optional[int] = None
    page: Optional[int] = None

class search_commits_params(msgspec.Struct):
    q: Optional[str] = None
    sort: Optional[str] = None
    order: Optional[str] = None
    per_page: Optional[int] = None
    page: Optional[int] = None

class search_issues_and_pull_requests_params(msgspec.Struct):
    q: Optional[str] = None
    sort: Optional[str] = None
    order: Optional[str] = None
    per_page: Optional[int] = None
    page: Optional[int] = None
    advanced_search: Optional[str] = None

class search_labels_params(msgspec.Struct):
    repository_id: Optional[int] = None
    q: Optional[str] = None
    sort: Optional[str] = None
    order: Optional[str] = None
    per_page: Optional[int] = None
    page: Optional[int] = None

class search_repos_params(msgspec.Struct):
    q: Optional[str] = None
    sort: Optional[str] = None
    order: Optional[str] = None
    per_page: Optional[int] = None
    page: Optional[int] = None

class search_topics_params(msgspec.Struct):
    q: Optional[str] = None
    per_page: Optional[int] = None
    page: Optional[int] = None

class search_users_params(msgspec.Struct):
    q: Optional[str] = None
    sort: Optional[str] = None
    order: Optional[str] = None
    per_page: Optional[int] = None
    page: Optional[int] = None

class teams_get_legacy_params(msgspec.Struct):
    team_id: Optional[int] = None

class teams_update_legacy_params(msgspec.Struct):
    team_id: Optional[int] = None
    name: Optional[Any] = None
    description: Optional[Any] = None
    privacy: Optional[Any] = None
    notification_setting: Optional[Any] = None
    permission: Optional[Any] = None
    parent_team_id: Optional[Any] = None

class teams_delete_legacy_params(msgspec.Struct):
    team_id: Optional[int] = None

class teams_list_discussions_legacy_params(msgspec.Struct):
    team_id: Optional[int] = None
    direction: Optional[str] = None
    per_page: Optional[int] = None
    page: Optional[int] = None

class teams_create_discussion_legacy_params(msgspec.Struct):
    team_id: Optional[int] = None
    title: Optional[Any] = None
    body: Optional[Any] = None
    private: Optional[Any] = None

class teams_get_discussion_legacy_params(msgspec.Struct):
    team_id: Optional[int] = None
    discussion_number: Optional[int] = None

class teams_update_discussion_legacy_params(msgspec.Struct):
    team_id: Optional[int] = None
    discussion_number: Optional[int] = None
    title: Optional[Any] = None
    body: Optional[Any] = None

class teams_delete_discussion_legacy_params(msgspec.Struct):
    team_id: Optional[int] = None
    discussion_number: Optional[int] = None

class teams_list_discussion_comments_legacy_params(msgspec.Struct):
    team_id: Optional[int] = None
    discussion_number: Optional[int] = None
    direction: Optional[str] = None
    per_page: Optional[int] = None
    page: Optional[int] = None

class teams_create_discussion_comment_legacy_params(msgspec.Struct):
    team_id: Optional[int] = None
    discussion_number: Optional[int] = None
    body: Optional[Any] = None

class teams_get_discussion_comment_legacy_params(msgspec.Struct):
    team_id: Optional[int] = None
    discussion_number: Optional[int] = None
    comment_number: Optional[int] = None

class teams_update_discussion_comment_legacy_params(msgspec.Struct):
    team_id: Optional[int] = None
    discussion_number: Optional[int] = None
    comment_number: Optional[int] = None
    body: Optional[Any] = None

class teams_delete_discussion_comment_legacy_params(msgspec.Struct):
    team_id: Optional[int] = None
    discussion_number: Optional[int] = None
    comment_number: Optional[int] = None

class reactions_list_for_team_discussion_comment_legacy_params(msgspec.Struct):
    team_id: Optional[int] = None
    discussion_number: Optional[int] = None
    comment_number: Optional[int] = None
    content: Optional[str] = None
    per_page: Optional[int] = None
    page: Optional[int] = None

class reactions_create_for_team_discussion_comment_legacy_params(msgspec.Struct):
    team_id: Optional[int] = None
    discussion_number: Optional[int] = None
    comment_number: Optional[int] = None
    content: Optional[Any] = None

class reactions_list_for_team_discussion_legacy_params(msgspec.Struct):
    team_id: Optional[int] = None
    discussion_number: Optional[int] = None
    content: Optional[str] = None
    per_page: Optional[int] = None
    page: Optional[int] = None

class reactions_create_for_team_discussion_legacy_params(msgspec.Struct):
    team_id: Optional[int] = None
    discussion_number: Optional[int] = None
    content: Optional[Any] = None

class teams_list_pending_invitations_legacy_params(msgspec.Struct):
    team_id: Optional[int] = None
    per_page: Optional[int] = None
    page: Optional[int] = None

class teams_list_members_legacy_params(msgspec.Struct):
    team_id: Optional[int] = None
    role: Optional[str] = None
    per_page: Optional[int] = None
    page: Optional[int] = None

class teams_get_member_legacy_params(msgspec.Struct):
    team_id: Optional[int] = None
    username: Optional[str] = None

class teams_add_member_legacy_params(msgspec.Struct):
    team_id: Optional[int] = None
    username: Optional[str] = None

class teams_remove_member_legacy_params(msgspec.Struct):
    team_id: Optional[int] = None
    username: Optional[str] = None

class teams_get_membership_for_user_legacy_params(msgspec.Struct):
    team_id: Optional[int] = None
    username: Optional[str] = None

class teams_add_or_update_membership_for_user_legacy_params(msgspec.Struct):
    team_id: Optional[int] = None
    username: Optional[str] = None
    role: Optional[Any] = None

class teams_remove_membership_for_user_legacy_params(msgspec.Struct):
    team_id: Optional[int] = None
    username: Optional[str] = None

class teams_list_projects_legacy_params(msgspec.Struct):
    team_id: Optional[int] = None
    per_page: Optional[int] = None
    page: Optional[int] = None

class teams_check_permissions_for_project_legacy_params(msgspec.Struct):
    team_id: Optional[int] = None
    project_id: Optional[int] = None

class teams_add_or_update_project_permissions_legacy_params(msgspec.Struct):
    team_id: Optional[int] = None
    project_id: Optional[int] = None
    permission: Optional[Any] = None

class teams_remove_project_legacy_params(msgspec.Struct):
    team_id: Optional[int] = None
    project_id: Optional[int] = None

class teams_list_repos_legacy_params(msgspec.Struct):
    team_id: Optional[int] = None
    per_page: Optional[int] = None
    page: Optional[int] = None

class teams_check_permissions_for_repo_legacy_params(msgspec.Struct):
    team_id: Optional[int] = None
    owner: Optional[str] = None
    repo: Optional[str] = None

class teams_add_or_update_repo_permissions_legacy_params(msgspec.Struct):
    team_id: Optional[int] = None
    owner: Optional[str] = None
    repo: Optional[str] = None
    permission: Optional[Any] = None

class teams_remove_repo_legacy_params(msgspec.Struct):
    team_id: Optional[int] = None
    owner: Optional[str] = None
    repo: Optional[str] = None

class teams_list_child_legacy_params(msgspec.Struct):
    team_id: Optional[int] = None
    per_page: Optional[int] = None
    page: Optional[int] = None

class users_get_authenticated_params(msgspec.Struct):
    pass

class users_update_authenticated_params(msgspec.Struct):
    name: Optional[Any] = None
    email: Optional[Any] = None
    blog: Optional[Any] = None
    twitter_username: Optional[Any] = None
    company: Optional[Any] = None
    location: Optional[Any] = None
    hireable: Optional[Any] = None
    bio: Optional[Any] = None

class users_list_blocked_by_authenticated_user_params(msgspec.Struct):
    per_page: Optional[int] = None
    page: Optional[int] = None

class users_check_blocked_params(msgspec.Struct):
    username: Optional[str] = None

class users_block_params(msgspec.Struct):
    username: Optional[str] = None

class users_unblock_params(msgspec.Struct):
    username: Optional[str] = None

class codespaces_list_for_authenticated_user_params(msgspec.Struct):
    per_page: Optional[int] = None
    page: Optional[int] = None
    repository_id: Optional[int] = None

class codespaces_create_for_authenticated_user_params(msgspec.Struct):
    pass

class codespaces_list_secrets_for_authenticated_user_params(msgspec.Struct):
    per_page: Optional[int] = None
    page: Optional[int] = None

class codespaces_get_public_key_for_authenticated_user_params(msgspec.Struct):
    pass

class codespaces_get_secret_for_authenticated_user_params(msgspec.Struct):
    secret_name: Optional[str] = None

class codespaces_create_or_update_secret_for_authenticated_user_params(msgspec.Struct):
    secret_name: Optional[str] = None
    encrypted_value: Optional[Any] = None
    key_id: Optional[Any] = None
    selected_repository_ids: Optional[Any] = None

class codespaces_delete_secret_for_authenticated_user_params(msgspec.Struct):
    secret_name: Optional[str] = None

class codespaces_list_repositories_for_secret_for_authenticated_user_params(msgspec.Struct):
    secret_name: Optional[str] = None

class codespaces_set_repositories_for_secret_for_authenticated_user_params(msgspec.Struct):
    secret_name: Optional[str] = None
    selected_repository_ids: Optional[Any] = None

class codespaces_add_repository_for_secret_for_authenticated_user_params(msgspec.Struct):
    secret_name: Optional[str] = None
    repository_id: Optional[int] = None

class codespaces_remove_repository_for_secret_for_authenticated_user_params(msgspec.Struct):
    secret_name: Optional[str] = None
    repository_id: Optional[int] = None

class codespaces_get_for_authenticated_user_params(msgspec.Struct):
    codespace_name: Optional[str] = None

class codespaces_update_for_authenticated_user_params(msgspec.Struct):
    codespace_name: Optional[str] = None
    machine: Optional[Any] = None
    display_name: Optional[Any] = None
    recent_folders: Optional[Any] = None

class codespaces_delete_for_authenticated_user_params(msgspec.Struct):
    codespace_name: Optional[str] = None

class codespaces_export_for_authenticated_user_params(msgspec.Struct):
    codespace_name: Optional[str] = None

class codespaces_get_export_details_for_authenticated_user_params(msgspec.Struct):
    codespace_name: Optional[str] = None
    export_id: Optional[str] = None

class codespaces_codespace_machines_for_authenticated_user_params(msgspec.Struct):
    codespace_name: Optional[str] = None

class codespaces_publish_for_authenticated_user_params(msgspec.Struct):
    codespace_name: Optional[str] = None
    name: Optional[Any] = None
    private: Optional[Any] = None

class codespaces_start_for_authenticated_user_params(msgspec.Struct):
    codespace_name: Optional[str] = None

class codespaces_stop_for_authenticated_user_params(msgspec.Struct):
    codespace_name: Optional[str] = None

class packages_list_docker_migration_conflicting_packages_for_authenticated_user_params(msgspec.Struct):
    pass

class users_set_primary_email_visibility_for_authenticated_user_params(msgspec.Struct):
    visibility: Optional[Any] = None

class users_list_emails_for_authenticated_user_params(msgspec.Struct):
    per_page: Optional[int] = None
    page: Optional[int] = None

class users_add_email_for_authenticated_user_params(msgspec.Struct):
    pass

class users_delete_email_for_authenticated_user_params(msgspec.Struct):
    pass

class users_list_followers_for_authenticated_user_params(msgspec.Struct):
    per_page: Optional[int] = None
    page: Optional[int] = None

class users_list_followed_by_authenticated_user_params(msgspec.Struct):
    per_page: Optional[int] = None
    page: Optional[int] = None

class users_check_person_is_followed_by_authenticated_params(msgspec.Struct):
    username: Optional[str] = None

class users_follow_params(msgspec.Struct):
    username: Optional[str] = None

class users_unfollow_params(msgspec.Struct):
    username: Optional[str] = None

class users_list_gpg_keys_for_authenticated_user_params(msgspec.Struct):
    per_page: Optional[int] = None
    page: Optional[int] = None

class users_create_gpg_key_for_authenticated_user_params(msgspec.Struct):
    name: Optional[Any] = None
    armored_public_key: Optional[Any] = None

class users_get_gpg_key_for_authenticated_user_params(msgspec.Struct):
    gpg_key_id: Optional[int] = None

class users_delete_gpg_key_for_authenticated_user_params(msgspec.Struct):
    gpg_key_id: Optional[int] = None

class apps_list_installations_for_authenticated_user_params(msgspec.Struct):
    per_page: Optional[int] = None
    page: Optional[int] = None

class apps_list_installation_repos_for_authenticated_user_params(msgspec.Struct):
    installation_id: Optional[int] = None
    per_page: Optional[int] = None
    page: Optional[int] = None

class apps_add_repo_to_installation_for_authenticated_user_params(msgspec.Struct):
    installation_id: Optional[int] = None
    repository_id: Optional[int] = None

class apps_remove_repo_from_installation_for_authenticated_user_params(msgspec.Struct):
    installation_id: Optional[int] = None
    repository_id: Optional[int] = None

class interactions_get_restrictions_for_authenticated_user_params(msgspec.Struct):
    pass

class interactions_set_restrictions_for_authenticated_user_params(msgspec.Struct):
    limit: Optional[Any] = None
    expiry: Optional[Any] = None

class interactions_remove_restrictions_for_authenticated_user_params(msgspec.Struct):
    pass

class issues_list_for_authenticated_user_params(msgspec.Struct):
    filter: Optional[str] = None
    state: Optional[str] = None
    labels: Optional[str] = None
    sort: Optional[str] = None
    direction: Optional[str] = None
    since: Optional[str] = None
    per_page: Optional[int] = None
    page: Optional[int] = None

class users_list_public_ssh_keys_for_authenticated_user_params(msgspec.Struct):
    per_page: Optional[int] = None
    page: Optional[int] = None

class users_create_public_ssh_key_for_authenticated_user_params(msgspec.Struct):
    title: Optional[Any] = None
    key: Optional[Any] = None

class users_get_public_ssh_key_for_authenticated_user_params(msgspec.Struct):
    key_id: Optional[int] = None

class users_delete_public_ssh_key_for_authenticated_user_params(msgspec.Struct):
    key_id: Optional[int] = None

class apps_list_subscriptions_for_authenticated_user_params(msgspec.Struct):
    per_page: Optional[int] = None
    page: Optional[int] = None

class apps_list_subscriptions_for_authenticated_user_stubbed_params(msgspec.Struct):
    per_page: Optional[int] = None
    page: Optional[int] = None

class orgs_list_memberships_for_authenticated_user_params(msgspec.Struct):
    state: Optional[str] = None
    per_page: Optional[int] = None
    page: Optional[int] = None

class orgs_get_membership_for_authenticated_user_params(msgspec.Struct):
    org: Optional[str] = None

class orgs_update_membership_for_authenticated_user_params(msgspec.Struct):
    org: Optional[str] = None
    state: Optional[Any] = None

class migrations_list_for_authenticated_user_params(msgspec.Struct):
    per_page: Optional[int] = None
    page: Optional[int] = None

class migrations_start_for_authenticated_user_params(msgspec.Struct):
    lock_repositories: Optional[Any] = None
    exclude_metadata: Optional[Any] = None
    exclude_git_data: Optional[Any] = None
    exclude_attachments: Optional[Any] = None
    exclude_releases: Optional[Any] = None
    exclude_owner_projects: Optional[Any] = None
    org_metadata_only: Optional[Any] = None
    exclude: Optional[Any] = None
    repositories: Optional[Any] = None

class migrations_get_status_for_authenticated_user_params(msgspec.Struct):
    migration_id: Optional[int] = None
    exclude: Optional[List[str]] = None

class migrations_get_archive_for_authenticated_user_params(msgspec.Struct):
    migration_id: Optional[int] = None

class migrations_delete_archive_for_authenticated_user_params(msgspec.Struct):
    migration_id: Optional[int] = None

class migrations_unlock_repo_for_authenticated_user_params(msgspec.Struct):
    migration_id: Optional[int] = None
    repo_name: Optional[str] = None

class migrations_list_repos_for_authenticated_user_params(msgspec.Struct):
    migration_id: Optional[int] = None
    per_page: Optional[int] = None
    page: Optional[int] = None

class orgs_list_for_authenticated_user_params(msgspec.Struct):
    per_page: Optional[int] = None
    page: Optional[int] = None

class packages_list_packages_for_authenticated_user_params(msgspec.Struct):
    package_type: Optional[str] = None
    visibility: Optional[str] = None
    page: Optional[int] = None
    per_page: Optional[int] = None

class packages_get_package_for_authenticated_user_params(msgspec.Struct):
    package_type: Optional[str] = None
    package_name: Optional[str] = None

class packages_delete_package_for_authenticated_user_params(msgspec.Struct):
    package_type: Optional[str] = None
    package_name: Optional[str] = None

class packages_restore_package_for_authenticated_user_params(msgspec.Struct):
    package_type: Optional[str] = None
    package_name: Optional[str] = None
    token: Optional[str] = None

class packages_get_all_package_versions_for_package_owned_by_authenticated_user_params(msgspec.Struct):
    package_type: Optional[str] = None
    package_name: Optional[str] = None
    page: Optional[int] = None
    per_page: Optional[int] = None
    state: Optional[str] = None

class packages_get_package_version_for_authenticated_user_params(msgspec.Struct):
    package_type: Optional[str] = None
    package_name: Optional[str] = None
    package_version_id: Optional[int] = None

class packages_delete_package_version_for_authenticated_user_params(msgspec.Struct):
    package_type: Optional[str] = None
    package_name: Optional[str] = None
    package_version_id: Optional[int] = None

class packages_restore_package_version_for_authenticated_user_params(msgspec.Struct):
    package_type: Optional[str] = None
    package_name: Optional[str] = None
    package_version_id: Optional[int] = None

class projects_classic_create_for_authenticated_user_params(msgspec.Struct):
    name: Optional[Any] = None
    body: Optional[Any] = None

class users_list_public_emails_for_authenticated_user_params(msgspec.Struct):
    per_page: Optional[int] = None
    page: Optional[int] = None

class repos_list_for_authenticated_user_params(msgspec.Struct):
    visibility: Optional[str] = None
    affiliation: Optional[str] = None
    type: Optional[str] = None
    sort: Optional[str] = None
    direction: Optional[str] = None
    per_page: Optional[int] = None
    page: Optional[int] = None
    since: Optional[str] = None
    before: Optional[str] = None

class repos_create_for_authenticated_user_params(msgspec.Struct):
    name: Optional[Any] = None
    description: Optional[Any] = None
    homepage: Optional[Any] = None
    private: Optional[Any] = None
    has_issues: Optional[Any] = None
    has_projects: Optional[Any] = None
    has_wiki: Optional[Any] = None
    has_discussions: Optional[Any] = None
    team_id: Optional[Any] = None
    auto_init: Optional[Any] = None
    gitignore_template: Optional[Any] = None
    license_template: Optional[Any] = None
    allow_squash_merge: Optional[Any] = None
    allow_merge_commit: Optional[Any] = None
    allow_rebase_merge: Optional[Any] = None
    allow_auto_merge: Optional[Any] = None
    delete_branch_on_merge: Optional[Any] = None
    squash_merge_commit_title: Optional[Any] = None
    squash_merge_commit_message: Optional[Any] = None
    merge_commit_title: Optional[Any] = None
    merge_commit_message: Optional[Any] = None
    has_downloads: Optional[Any] = None
    is_template: Optional[Any] = None

class repos_list_invitations_for_authenticated_user_params(msgspec.Struct):
    per_page: Optional[int] = None
    page: Optional[int] = None

class repos_accept_invitation_for_authenticated_user_params(msgspec.Struct):
    invitation_id: Optional[int] = None

class repos_decline_invitation_for_authenticated_user_params(msgspec.Struct):
    invitation_id: Optional[int] = None

class users_list_social_accounts_for_authenticated_user_params(msgspec.Struct):
    per_page: Optional[int] = None
    page: Optional[int] = None

class users_add_social_account_for_authenticated_user_params(msgspec.Struct):
    account_urls: Optional[Any] = None

class users_delete_social_account_for_authenticated_user_params(msgspec.Struct):
    account_urls: Optional[Any] = None

class users_list_ssh_signing_keys_for_authenticated_user_params(msgspec.Struct):
    per_page: Optional[int] = None
    page: Optional[int] = None

class users_create_ssh_signing_key_for_authenticated_user_params(msgspec.Struct):
    title: Optional[Any] = None
    key: Optional[Any] = None

class users_get_ssh_signing_key_for_authenticated_user_params(msgspec.Struct):
    ssh_signing_key_id: Optional[int] = None

class users_delete_ssh_signing_key_for_authenticated_user_params(msgspec.Struct):
    ssh_signing_key_id: Optional[int] = None

class activity_list_repos_starred_by_authenticated_user_params(msgspec.Struct):
    sort: Optional[str] = None
    direction: Optional[str] = None
    per_page: Optional[int] = None
    page: Optional[int] = None

class activity_check_repo_is_starred_by_authenticated_user_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None

class activity_star_repo_for_authenticated_user_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None

class activity_unstar_repo_for_authenticated_user_params(msgspec.Struct):
    owner: Optional[str] = None
    repo: Optional[str] = None

class activity_list_watched_repos_for_authenticated_user_params(msgspec.Struct):
    per_page: Optional[int] = None
    page: Optional[int] = None

class teams_list_for_authenticated_user_params(msgspec.Struct):
    per_page: Optional[int] = None
    page: Optional[int] = None

class users_get_by_id_params(msgspec.Struct):
    account_id: Optional[int] = None

class users_list_params(msgspec.Struct):
    since: Optional[int] = None
    per_page: Optional[int] = None

class users_get_by_username_params(msgspec.Struct):
    username: Optional[str] = None

class users_list_attestations_bulk_params(msgspec.Struct):
    per_page: Optional[int] = None
    before: Optional[str] = None
    after: Optional[str] = None
    username: Optional[str] = None
    subject_digests: Optional[Any] = None
    predicate_type: Optional[Any] = None

class users_delete_attestations_bulk_params(msgspec.Struct):
    username: Optional[str] = None

class users_delete_attestations_by_subject_digest_params(msgspec.Struct):
    username: Optional[str] = None
    subject_digest: Optional[str] = None

class users_delete_attestations_by_id_params(msgspec.Struct):
    username: Optional[str] = None
    attestation_id: Optional[int] = None

class users_list_attestations_params(msgspec.Struct):
    per_page: Optional[int] = None
    before: Optional[str] = None
    after: Optional[str] = None
    username: Optional[str] = None
    subject_digest: Optional[str] = None
    predicate_type: Optional[str] = None

class packages_list_docker_migration_conflicting_packages_for_user_params(msgspec.Struct):
    username: Optional[str] = None

class activity_list_events_for_authenticated_user_params(msgspec.Struct):
    username: Optional[str] = None
    per_page: Optional[int] = None
    page: Optional[int] = None

class activity_list_org_events_for_authenticated_user_params(msgspec.Struct):
    username: Optional[str] = None
    org: Optional[str] = None
    per_page: Optional[int] = None
    page: Optional[int] = None

class activity_list_public_events_for_user_params(msgspec.Struct):
    username: Optional[str] = None
    per_page: Optional[int] = None
    page: Optional[int] = None

class users_list_followers_for_user_params(msgspec.Struct):
    username: Optional[str] = None
    per_page: Optional[int] = None
    page: Optional[int] = None

class users_list_following_for_user_params(msgspec.Struct):
    username: Optional[str] = None
    per_page: Optional[int] = None
    page: Optional[int] = None

class users_check_following_for_user_params(msgspec.Struct):
    username: Optional[str] = None
    target_user: Optional[str] = None

class gists_list_for_user_params(msgspec.Struct):
    username: Optional[str] = None
    since: Optional[str] = None
    per_page: Optional[int] = None
    page: Optional[int] = None

class users_list_gpg_keys_for_user_params(msgspec.Struct):
    username: Optional[str] = None
    per_page: Optional[int] = None
    page: Optional[int] = None

class users_get_context_for_user_params(msgspec.Struct):
    username: Optional[str] = None
    subject_type: Optional[str] = None
    subject_id: Optional[str] = None

class apps_get_user_installation_params(msgspec.Struct):
    username: Optional[str] = None

class users_list_public_keys_for_user_params(msgspec.Struct):
    username: Optional[str] = None
    per_page: Optional[int] = None
    page: Optional[int] = None

class orgs_list_for_user_params(msgspec.Struct):
    username: Optional[str] = None
    per_page: Optional[int] = None
    page: Optional[int] = None

class packages_list_packages_for_user_params(msgspec.Struct):
    package_type: Optional[str] = None
    visibility: Optional[str] = None
    username: Optional[str] = None
    page: Optional[int] = None
    per_page: Optional[int] = None

class packages_get_package_for_user_params(msgspec.Struct):
    package_type: Optional[str] = None
    package_name: Optional[str] = None
    username: Optional[str] = None

class packages_delete_package_for_user_params(msgspec.Struct):
    package_type: Optional[str] = None
    package_name: Optional[str] = None
    username: Optional[str] = None

class packages_restore_package_for_user_params(msgspec.Struct):
    package_type: Optional[str] = None
    package_name: Optional[str] = None
    username: Optional[str] = None
    token: Optional[str] = None

class packages_get_all_package_versions_for_package_owned_by_user_params(msgspec.Struct):
    package_type: Optional[str] = None
    package_name: Optional[str] = None
    username: Optional[str] = None

class packages_get_package_version_for_user_params(msgspec.Struct):
    package_type: Optional[str] = None
    package_name: Optional[str] = None
    package_version_id: Optional[int] = None
    username: Optional[str] = None

class packages_delete_package_version_for_user_params(msgspec.Struct):
    package_type: Optional[str] = None
    package_name: Optional[str] = None
    username: Optional[str] = None
    package_version_id: Optional[int] = None

class packages_restore_package_version_for_user_params(msgspec.Struct):
    package_type: Optional[str] = None
    package_name: Optional[str] = None
    username: Optional[str] = None
    package_version_id: Optional[int] = None

class projects_classic_list_for_user_params(msgspec.Struct):
    username: Optional[str] = None
    state: Optional[str] = None
    per_page: Optional[int] = None
    page: Optional[int] = None

class activity_list_received_events_for_user_params(msgspec.Struct):
    username: Optional[str] = None
    per_page: Optional[int] = None
    page: Optional[int] = None

class activity_list_received_public_events_for_user_params(msgspec.Struct):
    username: Optional[str] = None
    per_page: Optional[int] = None
    page: Optional[int] = None

class repos_list_for_user_params(msgspec.Struct):
    username: Optional[str] = None
    type: Optional[str] = None
    sort: Optional[str] = None
    direction: Optional[str] = None
    per_page: Optional[int] = None
    page: Optional[int] = None

class billing_get_github_actions_billing_user_params(msgspec.Struct):
    username: Optional[str] = None

class billing_get_github_packages_billing_user_params(msgspec.Struct):
    username: Optional[str] = None

class billing_get_shared_storage_billing_user_params(msgspec.Struct):
    username: Optional[str] = None

class billing_get_github_billing_usage_report_user_params(msgspec.Struct):
    username: Optional[str] = None
    year: Optional[int] = None
    month: Optional[int] = None
    day: Optional[int] = None
    hour: Optional[int] = None

class users_list_social_accounts_for_user_params(msgspec.Struct):
    username: Optional[str] = None
    per_page: Optional[int] = None
    page: Optional[int] = None

class users_list_ssh_signing_keys_for_user_params(msgspec.Struct):
    username: Optional[str] = None
    per_page: Optional[int] = None
    page: Optional[int] = None

class activity_list_repos_starred_by_user_params(msgspec.Struct):
    username: Optional[str] = None
    sort: Optional[str] = None
    direction: Optional[str] = None
    per_page: Optional[int] = None
    page: Optional[int] = None

class activity_list_repos_watched_by_user_params(msgspec.Struct):
    username: Optional[str] = None
    per_page: Optional[int] = None
    page: Optional[int] = None

class meta_get_all_versions_params(msgspec.Struct):
    pass

class meta_get_zen_params(msgspec.Struct):
    pass
