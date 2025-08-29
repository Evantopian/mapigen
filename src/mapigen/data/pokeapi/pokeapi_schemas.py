import msgspec
from typing import Any, Optional, List

class api_v2_ability_list_params(msgspec.Struct):
    limit: Optional[int] = None
    offset: Optional[int] = None
    q: Optional[str] = None

class api_v2_ability_retrieve_params(msgspec.Struct):
    id: Optional[str] = None

class api_v2_berry_list_params(msgspec.Struct):
    limit: Optional[int] = None
    offset: Optional[int] = None
    q: Optional[str] = None

class api_v2_berry_retrieve_params(msgspec.Struct):
    id: Optional[str] = None

class api_v2_berry_firmness_list_params(msgspec.Struct):
    limit: Optional[int] = None
    offset: Optional[int] = None
    q: Optional[str] = None

class api_v2_berry_firmness_retrieve_params(msgspec.Struct):
    id: Optional[str] = None

class api_v2_berry_flavor_list_params(msgspec.Struct):
    limit: Optional[int] = None
    offset: Optional[int] = None
    q: Optional[str] = None

class api_v2_berry_flavor_retrieve_params(msgspec.Struct):
    id: Optional[str] = None

class api_v2_characteristic_list_params(msgspec.Struct):
    limit: Optional[int] = None
    offset: Optional[int] = None
    q: Optional[str] = None

class api_v2_characteristic_retrieve_params(msgspec.Struct):
    id: Optional[str] = None

class api_v2_contest_type_list_params(msgspec.Struct):
    limit: Optional[int] = None
    offset: Optional[int] = None
    q: Optional[str] = None

class api_v2_contest_type_retrieve_params(msgspec.Struct):
    id: Optional[str] = None

class api_v2_contest_effect_list_params(msgspec.Struct):
    limit: Optional[int] = None
    offset: Optional[int] = None
    q: Optional[str] = None

class api_v2_contest_effect_retrieve_params(msgspec.Struct):
    id: Optional[str] = None

class api_v2_egg_group_list_params(msgspec.Struct):
    limit: Optional[int] = None
    offset: Optional[int] = None
    q: Optional[str] = None

class api_v2_egg_group_retrieve_params(msgspec.Struct):
    id: Optional[str] = None

class api_v2_encounter_method_list_params(msgspec.Struct):
    limit: Optional[int] = None
    offset: Optional[int] = None
    q: Optional[str] = None

class api_v2_encounter_method_retrieve_params(msgspec.Struct):
    id: Optional[str] = None

class api_v2_encounter_condition_list_params(msgspec.Struct):
    limit: Optional[int] = None
    offset: Optional[int] = None
    q: Optional[str] = None

class api_v2_encounter_condition_retrieve_params(msgspec.Struct):
    id: Optional[str] = None

class api_v2_encounter_condition_value_list_params(msgspec.Struct):
    limit: Optional[int] = None
    offset: Optional[int] = None
    q: Optional[str] = None

class api_v2_encounter_condition_value_retrieve_params(msgspec.Struct):
    id: Optional[str] = None

class api_v2_evolution_chain_list_params(msgspec.Struct):
    limit: Optional[int] = None
    offset: Optional[int] = None
    q: Optional[str] = None

class api_v2_evolution_chain_retrieve_params(msgspec.Struct):
    id: Optional[str] = None

class api_v2_evolution_trigger_list_params(msgspec.Struct):
    limit: Optional[int] = None
    offset: Optional[int] = None
    q: Optional[str] = None

class api_v2_evolution_trigger_retrieve_params(msgspec.Struct):
    id: Optional[str] = None

class api_v2_generation_list_params(msgspec.Struct):
    limit: Optional[int] = None
    offset: Optional[int] = None
    q: Optional[str] = None

class api_v2_generation_retrieve_params(msgspec.Struct):
    id: Optional[str] = None

class api_v2_gender_list_params(msgspec.Struct):
    limit: Optional[int] = None
    offset: Optional[int] = None
    q: Optional[str] = None

class api_v2_gender_retrieve_params(msgspec.Struct):
    id: Optional[str] = None

class api_v2_growth_rate_list_params(msgspec.Struct):
    limit: Optional[int] = None
    offset: Optional[int] = None
    q: Optional[str] = None

class api_v2_growth_rate_retrieve_params(msgspec.Struct):
    id: Optional[str] = None

class api_v2_item_list_params(msgspec.Struct):
    limit: Optional[int] = None
    offset: Optional[int] = None
    q: Optional[str] = None

class api_v2_item_retrieve_params(msgspec.Struct):
    id: Optional[str] = None

class api_v2_item_category_list_params(msgspec.Struct):
    limit: Optional[int] = None
    offset: Optional[int] = None
    q: Optional[str] = None

class api_v2_item_category_retrieve_params(msgspec.Struct):
    id: Optional[str] = None

class api_v2_item_attribute_list_params(msgspec.Struct):
    limit: Optional[int] = None
    offset: Optional[int] = None
    q: Optional[str] = None

class api_v2_item_attribute_retrieve_params(msgspec.Struct):
    id: Optional[str] = None

class api_v2_item_fling_effect_list_params(msgspec.Struct):
    limit: Optional[int] = None
    offset: Optional[int] = None
    q: Optional[str] = None

class api_v2_item_fling_effect_retrieve_params(msgspec.Struct):
    id: Optional[str] = None

class api_v2_item_pocket_list_params(msgspec.Struct):
    limit: Optional[int] = None
    offset: Optional[int] = None
    q: Optional[str] = None

class api_v2_item_pocket_retrieve_params(msgspec.Struct):
    id: Optional[str] = None

class api_v2_language_list_params(msgspec.Struct):
    limit: Optional[int] = None
    offset: Optional[int] = None
    q: Optional[str] = None

class api_v2_language_retrieve_params(msgspec.Struct):
    id: Optional[str] = None

class api_v2_location_list_params(msgspec.Struct):
    limit: Optional[int] = None
    offset: Optional[int] = None
    q: Optional[str] = None

class api_v2_location_retrieve_params(msgspec.Struct):
    id: Optional[str] = None

class api_v2_location_area_list_params(msgspec.Struct):
    limit: Optional[int] = None
    offset: Optional[int] = None

class api_v2_location_area_retrieve_params(msgspec.Struct):
    id: Optional[int] = None

class api_v2_machine_list_params(msgspec.Struct):
    limit: Optional[int] = None
    offset: Optional[int] = None
    q: Optional[str] = None

class api_v2_machine_retrieve_params(msgspec.Struct):
    id: Optional[str] = None

class api_v2_move_list_params(msgspec.Struct):
    limit: Optional[int] = None
    offset: Optional[int] = None
    q: Optional[str] = None

class api_v2_move_retrieve_params(msgspec.Struct):
    id: Optional[str] = None

class api_v2_move_ailment_list_params(msgspec.Struct):
    limit: Optional[int] = None
    offset: Optional[int] = None
    q: Optional[str] = None

class api_v2_move_ailment_retrieve_params(msgspec.Struct):
    id: Optional[str] = None

class api_v2_move_battle_style_list_params(msgspec.Struct):
    limit: Optional[int] = None
    offset: Optional[int] = None
    q: Optional[str] = None

class api_v2_move_battle_style_retrieve_params(msgspec.Struct):
    id: Optional[str] = None

class api_v2_move_category_list_params(msgspec.Struct):
    limit: Optional[int] = None
    offset: Optional[int] = None
    q: Optional[str] = None

class api_v2_move_category_retrieve_params(msgspec.Struct):
    id: Optional[str] = None

class api_v2_move_damage_class_list_params(msgspec.Struct):
    limit: Optional[int] = None
    offset: Optional[int] = None
    q: Optional[str] = None

class api_v2_move_damage_class_retrieve_params(msgspec.Struct):
    id: Optional[str] = None

class api_v2_move_learn_method_list_params(msgspec.Struct):
    limit: Optional[int] = None
    offset: Optional[int] = None
    q: Optional[str] = None

class api_v2_move_learn_method_retrieve_params(msgspec.Struct):
    id: Optional[str] = None

class api_v2_move_target_list_params(msgspec.Struct):
    limit: Optional[int] = None
    offset: Optional[int] = None
    q: Optional[str] = None

class api_v2_move_target_retrieve_params(msgspec.Struct):
    id: Optional[str] = None

class api_v2_nature_list_params(msgspec.Struct):
    limit: Optional[int] = None
    offset: Optional[int] = None
    q: Optional[str] = None

class api_v2_nature_retrieve_params(msgspec.Struct):
    id: Optional[str] = None

class api_v2_pal_park_area_list_params(msgspec.Struct):
    limit: Optional[int] = None
    offset: Optional[int] = None
    q: Optional[str] = None

class api_v2_pal_park_area_retrieve_params(msgspec.Struct):
    id: Optional[str] = None

class api_v2_pokedex_list_params(msgspec.Struct):
    limit: Optional[int] = None
    offset: Optional[int] = None
    q: Optional[str] = None

class api_v2_pokedex_retrieve_params(msgspec.Struct):
    id: Optional[str] = None

class api_v2_pokemon_list_params(msgspec.Struct):
    limit: Optional[int] = None
    offset: Optional[int] = None
    q: Optional[str] = None

class api_v2_pokemon_retrieve_params(msgspec.Struct):
    id: Optional[str] = None

class api_v2_pokemon_color_list_params(msgspec.Struct):
    limit: Optional[int] = None
    offset: Optional[int] = None
    q: Optional[str] = None

class api_v2_pokemon_color_retrieve_params(msgspec.Struct):
    id: Optional[str] = None

class api_v2_pokemon_form_list_params(msgspec.Struct):
    limit: Optional[int] = None
    offset: Optional[int] = None
    q: Optional[str] = None

class api_v2_pokemon_form_retrieve_params(msgspec.Struct):
    id: Optional[str] = None

class api_v2_pokemon_habitat_list_params(msgspec.Struct):
    limit: Optional[int] = None
    offset: Optional[int] = None
    q: Optional[str] = None

class api_v2_pokemon_habitat_retrieve_params(msgspec.Struct):
    id: Optional[str] = None

class api_v2_pokemon_shape_list_params(msgspec.Struct):
    limit: Optional[int] = None
    offset: Optional[int] = None
    q: Optional[str] = None

class api_v2_pokemon_shape_retrieve_params(msgspec.Struct):
    id: Optional[str] = None

class api_v2_pokemon_species_list_params(msgspec.Struct):
    limit: Optional[int] = None
    offset: Optional[int] = None
    q: Optional[str] = None

class api_v2_pokemon_species_retrieve_params(msgspec.Struct):
    id: Optional[str] = None

class api_v2_pokeathlon_stat_list_params(msgspec.Struct):
    limit: Optional[int] = None
    offset: Optional[int] = None
    q: Optional[str] = None

class api_v2_pokeathlon_stat_retrieve_params(msgspec.Struct):
    id: Optional[str] = None

class api_v2_region_list_params(msgspec.Struct):
    limit: Optional[int] = None
    offset: Optional[int] = None
    q: Optional[str] = None

class api_v2_region_retrieve_params(msgspec.Struct):
    id: Optional[str] = None

class api_v2_stat_list_params(msgspec.Struct):
    limit: Optional[int] = None
    offset: Optional[int] = None
    q: Optional[str] = None

class api_v2_stat_retrieve_params(msgspec.Struct):
    id: Optional[str] = None

class api_v2_super_contest_effect_list_params(msgspec.Struct):
    limit: Optional[int] = None
    offset: Optional[int] = None
    q: Optional[str] = None

class api_v2_super_contest_effect_retrieve_params(msgspec.Struct):
    id: Optional[str] = None

class api_v2_type_list_params(msgspec.Struct):
    limit: Optional[int] = None
    offset: Optional[int] = None
    q: Optional[str] = None

class api_v2_type_retrieve_params(msgspec.Struct):
    id: Optional[str] = None

class api_v2_version_list_params(msgspec.Struct):
    limit: Optional[int] = None
    offset: Optional[int] = None
    q: Optional[str] = None

class api_v2_version_retrieve_params(msgspec.Struct):
    id: Optional[str] = None

class api_v2_version_group_list_params(msgspec.Struct):
    limit: Optional[int] = None
    offset: Optional[int] = None
    q: Optional[str] = None

class api_v2_version_group_retrieve_params(msgspec.Struct):
    id: Optional[str] = None

class api_v2_pokemon_encounters_retrieve_params(msgspec.Struct):
    pokemon_id: Optional[str] = None
