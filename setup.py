import cx_Freeze

executables = [cx_Freeze.Executable("space_invaders.py")]

cx_Freeze.setup(
    name="Space Invaders",
    options={"build_exe": {"packages":["pygame"],
                           "include_files":["res"]}},
    executables = executables

    )