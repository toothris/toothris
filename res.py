import res_game_032x032_acid_drop
import res_game_032x032_i_frag
import res_game_032x032_j_frag
import res_game_032x032_l_frag
import res_game_032x032_o_frag
import res_game_032x032_s_frag
import res_game_032x032_t_frag
import res_game_032x032_z_frag
import res_game_064x064_down
import res_game_064x064_left
import res_game_064x064_o
import res_game_064x064_pause
import res_game_064x064_right
import res_game_064x064_rotate
import res_game_064x064_selected1
import res_game_064x064_selected2
import res_game_064x064_selected3
import res_game_064x064_selected4
import res_game_096x096_j
import res_game_096x096_l
import res_game_096x096_s
import res_game_096x096_t
import res_game_096x096_z
import res_game_128x128_bonus_acid_rain
import res_game_128x128_bonus_builder
import res_game_128x128_bonus_earthquake
import res_game_128x128_bonus_hail
import res_game_128x128_bonus_king_of_hill
import res_game_128x128_bonus_super_drop
import res_game_128x128_bonus_super_hit
import res_game_128x128_event_drop
import res_game_128x128_event_float
import res_game_128x128_event_frag
import res_game_128x128_event_ground
import res_game_128x128_event_hit
import res_game_128x128_event_rotate
import res_game_128x128_event_swallow
import res_game_128x128_i
import res_game_256x512_stakan
import res_ui_about_256x256_logo
import res_ui_menu_064x064_lines1
import res_ui_menu_064x064_lines2
import res_ui_menu_064x064_lines3
import res_ui_menu_064x064_lines4
import res_ui_menu_064x064_sparks1
import res_ui_menu_064x064_sparks2
import res_ui_menu_064x064_sparks3
import res_ui_menu_064x064_sparks4
import res_ui_menu_064x064_splat1
import res_ui_menu_064x064_splat2
import res_ui_menu_064x064_splat3
import res_ui_menu_064x064_splat4
import res_ui_menu_064x064_star1
import res_ui_menu_064x064_star2
import res_ui_menu_064x064_star3
import res_ui_menu_064x064_star4
import res_ui_menu_256x064_about
import res_ui_menu_256x064_exit
import res_ui_menu_256x064_new_game
import res_ui_menu_256x064_options
import res_ui_menu_256x064_selected1
import res_ui_menu_256x064_selected2
import res_ui_menu_256x064_selected3
import res_ui_menu_256x064_selected4
import res_ui_menu_256x256_back
import res_ui_options_064x064_pointer
import res_ui_options_256x064_music
import res_ui_options_256x064_music_off
import res_ui_options_256x064_sound
import res_ui_options_256x064_sound_off

lookup = \
    { res_game_032x032_acid_drop.name : res_game_032x032_acid_drop
    , res_game_032x032_i_frag.name : res_game_032x032_i_frag
    , res_game_032x032_j_frag.name : res_game_032x032_j_frag
    , res_game_032x032_l_frag.name : res_game_032x032_l_frag
    , res_game_032x032_o_frag.name : res_game_032x032_o_frag
    , res_game_032x032_s_frag.name : res_game_032x032_s_frag
    , res_game_032x032_t_frag.name : res_game_032x032_t_frag
    , res_game_032x032_z_frag.name : res_game_032x032_z_frag
    , res_game_064x064_down.name : res_game_064x064_down
    , res_game_064x064_left.name : res_game_064x064_left
    , res_game_064x064_o.name : res_game_064x064_o
    , res_game_064x064_pause.name : res_game_064x064_pause
    , res_game_064x064_right.name : res_game_064x064_right
    , res_game_064x064_rotate.name : res_game_064x064_rotate
    , res_game_064x064_selected1.name : res_game_064x064_selected1
    , res_game_064x064_selected2.name : res_game_064x064_selected2
    , res_game_064x064_selected3.name : res_game_064x064_selected3
    , res_game_064x064_selected4.name : res_game_064x064_selected4
    , res_game_096x096_j.name : res_game_096x096_j
    , res_game_096x096_l.name : res_game_096x096_l
    , res_game_096x096_s.name : res_game_096x096_s
    , res_game_096x096_t.name : res_game_096x096_t
    , res_game_096x096_z.name : res_game_096x096_z
    , res_game_128x128_bonus_acid_rain.name : res_game_128x128_bonus_acid_rain
    , res_game_128x128_bonus_builder.name : res_game_128x128_bonus_builder
    , res_game_128x128_bonus_earthquake.name : res_game_128x128_bonus_earthquake
    , res_game_128x128_bonus_hail.name : res_game_128x128_bonus_hail
    , res_game_128x128_bonus_king_of_hill.name : res_game_128x128_bonus_king_of_hill
    , res_game_128x128_bonus_super_drop.name : res_game_128x128_bonus_super_drop
    , res_game_128x128_bonus_super_hit.name : res_game_128x128_bonus_super_hit
    , res_game_128x128_event_drop.name : res_game_128x128_event_drop
    , res_game_128x128_event_float.name : res_game_128x128_event_float
    , res_game_128x128_event_frag.name : res_game_128x128_event_frag
    , res_game_128x128_event_ground.name : res_game_128x128_event_ground
    , res_game_128x128_event_hit.name : res_game_128x128_event_hit
    , res_game_128x128_event_rotate.name : res_game_128x128_event_rotate
    , res_game_128x128_event_swallow.name : res_game_128x128_event_swallow
    , res_game_128x128_i.name : res_game_128x128_i
    , res_game_256x512_stakan.name : res_game_256x512_stakan
    , res_ui_about_256x256_logo.name : res_ui_about_256x256_logo
    , res_ui_menu_064x064_lines1.name : res_ui_menu_064x064_lines1
    , res_ui_menu_064x064_lines2.name : res_ui_menu_064x064_lines2
    , res_ui_menu_064x064_lines3.name : res_ui_menu_064x064_lines3
    , res_ui_menu_064x064_lines4.name : res_ui_menu_064x064_lines4
    , res_ui_menu_064x064_sparks1.name : res_ui_menu_064x064_sparks1
    , res_ui_menu_064x064_sparks2.name : res_ui_menu_064x064_sparks2
    , res_ui_menu_064x064_sparks3.name : res_ui_menu_064x064_sparks3
    , res_ui_menu_064x064_sparks4.name : res_ui_menu_064x064_sparks4
    , res_ui_menu_064x064_splat1.name : res_ui_menu_064x064_splat1
    , res_ui_menu_064x064_splat2.name : res_ui_menu_064x064_splat2
    , res_ui_menu_064x064_splat3.name : res_ui_menu_064x064_splat3
    , res_ui_menu_064x064_splat4.name : res_ui_menu_064x064_splat4
    , res_ui_menu_064x064_star1.name : res_ui_menu_064x064_star1
    , res_ui_menu_064x064_star2.name : res_ui_menu_064x064_star2
    , res_ui_menu_064x064_star3.name : res_ui_menu_064x064_star3
    , res_ui_menu_064x064_star4.name : res_ui_menu_064x064_star4
    , res_ui_menu_256x064_about.name : res_ui_menu_256x064_about
    , res_ui_menu_256x064_exit.name : res_ui_menu_256x064_exit
    , res_ui_menu_256x064_new_game.name : res_ui_menu_256x064_new_game
    , res_ui_menu_256x064_options.name : res_ui_menu_256x064_options
    , res_ui_menu_256x064_selected1.name : res_ui_menu_256x064_selected1
    , res_ui_menu_256x064_selected2.name : res_ui_menu_256x064_selected2
    , res_ui_menu_256x064_selected3.name : res_ui_menu_256x064_selected3
    , res_ui_menu_256x064_selected4.name : res_ui_menu_256x064_selected4
    , res_ui_menu_256x256_back.name : res_ui_menu_256x256_back
    , res_ui_options_064x064_pointer.name : res_ui_options_064x064_pointer
    , res_ui_options_256x064_music.name : res_ui_options_256x064_music
    , res_ui_options_256x064_music_off.name : res_ui_options_256x064_music_off
    , res_ui_options_256x064_sound.name : res_ui_options_256x064_sound
    , res_ui_options_256x064_sound_off.name : res_ui_options_256x064_sound_off
    }
