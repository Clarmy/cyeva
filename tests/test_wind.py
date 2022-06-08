from cyeva.core.wind import (
    get_least_angle_deflection,
    identify_direction,
    identify_wind_scale,
    get_least_lev_diff,
    get_least_dir_deflection,
    filter_wind_speed_levels,
    WindComparison,
)

from .case.wind import (
    LEAST_ANGLE_DEFLECTION_CASE,
    LEAST_DIR_DEFLECTION_CASE,
    IDENTIFY_DIRECTION8_CASE,
    WIND_DIR_SCORE_CASE,
    WIND_DIR_ACCURACY_RATE,
    IDENTIFY_SPEED_LEVEL_GENERAL_CASE,
    LEAST_LEV_DEFLECTION_CASE,
    WIND_LEVEL_ACCURACY_RATE_CASE,
    WIND_SPEED_SCORE_CASE,
    WIND_SPEED_ACCURACY_RATE_CASE,
    WIND_SPEED_MAE_CASE,
    WIND_SPEED_STRONGER_RATE_CASE,
    WIND_SPEED_WEAKER_RATE_CASE,
    WIND_SPEED_CHI_SQUARE_CASE,
    WIND_SPEED_RESIDUAL_SUM_OF_SQUARE_CASE,
    WIND_SPEED_LINREGRESS_CASE,
)


def test_get_least_angle_deflection():
    for case in LEAST_ANGLE_DEFLECTION_CASE:
        angle1 = case["angle1"]
        angle2 = case["angle2"]
        result = case["result"]
        assert get_least_angle_deflection(angle1, angle2) == result


def test_get_least_dir_deflection():
    for case in LEAST_DIR_DEFLECTION_CASE:
        dir1 = case["dir1"]
        dir2 = case["dir2"]
        result = case["result"]
        assert get_least_dir_deflection(dir1, dir2) == result


def test_identify_direction8():
    for case in IDENTIFY_DIRECTION8_CASE:
        angle = case["angle"]
        result = case["result"]
        assert identify_direction(angle, dnum=8) == result


def test_identify_wind_scale():
    for case in IDENTIFY_SPEED_LEVEL_GENERAL_CASE:
        wspd = case["wspd"]
        result = case["result"]
        assert identify_wind_scale(wspd) == result


def test_calc_wind_dir_score():
    for case in WIND_DIR_SCORE_CASE:
        obs = case["obs"]
        fct = case["fct"]
        result = case["result"]

        wind_comparison = WindComparison(obs_dir=obs, fct_dir=fct)

        assert wind_comparison.calc_dir_score() == result


def test_get_least_lev_deflection2():
    for case in LEAST_LEV_DEFLECTION_CASE:
        lev1 = case["lev1"]
        lev2 = case["lev2"]
        result = case["result"]
        assert get_least_lev_diff(lev1, lev2) == result


def test_calc_wind_dir_accuracy_ratio():
    for case in WIND_DIR_ACCURACY_RATE:
        obs = case["obs"]
        fct = case["fct"]
        result = case["result"]

        wind_comparison = WindComparison(obs_dir=obs, fct_dir=fct)

        assert wind_comparison.calc_dir_accuracy_ratio() == result


def test_calc_wind_scale_accuracy_ratio():
    for case in WIND_LEVEL_ACCURACY_RATE_CASE:
        obs = case["obs"]
        fct = case["fct"]
        result = case["result"]

        wind_comparison = WindComparison(obs_spd=obs, fct_spd=fct)

        assert wind_comparison.calc_level_accuracy_ratio() == result


def test_calc_wind_speed_accuracy_ratio():
    for case in WIND_SPEED_ACCURACY_RATE_CASE:
        obs = case["obs"]
        fct = case["fct"]
        result = case["result"]

        wind_comparison = WindComparison(obs_spd=obs, fct_spd=fct)

        assert wind_comparison.calc_speed_accuracy_ratio() == result


def test_calc_wind_speed_score():
    for case in WIND_SPEED_SCORE_CASE:
        obs = case["obs"]
        fct = case["fct"]
        result = case["result"]

        wind_comparison = WindComparison(obs_spd=obs, fct_spd=fct)

        assert wind_comparison.calc_speed_score() == result


def test_calc_wind_speed_level_stronger_ratio():
    for case in WIND_SPEED_STRONGER_RATE_CASE:
        obs = case["obs"]
        fct = case["fct"]
        result = case["result"]

        wind_comparison = WindComparison(obs_spd=obs, fct_spd=fct)

        assert wind_comparison.calc_speed_level_stronger_ratio() == result


def test_calc_wind_speed_level_weaker_ratio():
    for case in WIND_SPEED_WEAKER_RATE_CASE:
        obs = case["obs"]
        fct = case["fct"]
        result = case["result"]

        wind_comparison = WindComparison(obs_spd=obs, fct_spd=fct)

        assert wind_comparison.calc_speed_level_weaker_ratio() == result


def test_calc_wind_speed_chi_square():
    for case in WIND_SPEED_CHI_SQUARE_CASE:
        obs = case["obs"]
        fct = case["fct"]
        result = case["result"]

        wind_comparison = WindComparison(obs_spd=obs, fct_spd=fct)

        assert wind_comparison.calc_chi_square() == result


def test_calc_wind_speed_rss():
    for case in WIND_SPEED_RESIDUAL_SUM_OF_SQUARE_CASE:
        obs = case["obs"]
        fct = case["fct"]
        result = case["result"]

        wind_comparison = WindComparison(obs_spd=obs, fct_spd=fct)

        assert wind_comparison.calc_rss() == result


def test_calc_wind_speed_mae():
    for case in WIND_SPEED_MAE_CASE:
        obs = case["obs"]
        fct = case["fct"]
        result = case["result"]

        wind_comparison = WindComparison(obs_spd=obs, fct_spd=fct)

        assert wind_comparison.calc_mae() == result


def test_calc_wind_speed_linregress():
    for case in WIND_SPEED_LINREGRESS_CASE:
        obs = case["obs"]
        fct = case["fct"]
        result = case["result"]

        wind_comparison = WindComparison(obs_spd=obs, fct_spd=fct)

        slope, intercept, *_ = wind_comparison.calc_linregress_args()

        assert slope == result["slope"]
        assert intercept == result["intercept"]
