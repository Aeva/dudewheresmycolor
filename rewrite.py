
import os.path


COLOR_HUE_A = 240
COLOR_NAME_A = "blue"

COLOR_HUE_B = 360
COLOR_NAME_B = "red"


assert(COLOR_HUE_A >= 0)
assert(COLOR_HUE_B <= 360)
assert(COLOR_HUE_A < COLOR_HUE_B)
COLOR_HUE_MIDPOINT = round((COLOR_HUE_B - COLOR_HUE_A) / 2 + COLOR_HUE_A)
assert(COLOR_HUE_A < COLOR_HUE_MIDPOINT)
assert(COLOR_HUE_B > COLOR_HUE_MIDPOINT)
COLOR_HUE_A = str(COLOR_HUE_A)
COLOR_HUE_B = str(COLOR_HUE_B)
COLOR_HUE_MIDPOINT = str(COLOR_HUE_MIDPOINT)
COLOR_TITLE_A = COLOR_NAME_A.title()
COLOR_TITLE_B = COLOR_NAME_B.title()

REWRITE_PATHS = (
    "analysis/Analyze_results.ipynb",
    "src/components/BlueGreenTest.vue",
    "src/components/Results.vue",
    "src/utils/glmUtils.js",
    "index.html")

SUBSTITUTIONS = tuple([(g, globals()[g]) for g in globals() if g.startswith("COLOR_")])

if __name__ == "__main__":
    print(f"{COLOR_TITLE_A} = {COLOR_HUE_A}")
    print(f"{COLOR_TITLE_B} = {COLOR_HUE_B}")
    print(f"Midpoint = {COLOR_HUE_MIDPOINT}")

    for path in REWRITE_PATHS:
        assert(os.path.isfile(path))

        with open(path, "r") as in_file:
            src = in_file.read()

        for SIGIL, REPLACEMENT in SUBSTITUTIONS:
            src = src.replace(SIGIL, REPLACEMENT)

        with open(path, "w") as out_file:
            out_file.write(src)
