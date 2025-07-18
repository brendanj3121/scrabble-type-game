import project
player = project.Player()

def test_validate():
    add = ["t", "e", "s", "t"]
    player.pull.extend(add)
    assert project.validate("test") == True
    assert project.validate("TEST") == True
    assert project.validate("Test") == True
    assert project.validate("Test.") == False
    assert project.validate("text") == False

def test_validate_blank():
    player.pull.clear()
    add = ["t", "e", " ", "t"]
    player.pull.extend(add)
    assert project.validate("test") == True
    assert project.validate("text") == True
    assert project.validate("tets") == True
    assert project.validate("tout") == False
    assert project.validate("yet") == True
    assert project.validate("tess") == False

def test_score():
    player.pull.clear()
    player.blanks.clear()
    add = ["t", "e", "s", "t" ,"e", "d"]
    player.pull.extend(add)
    assert project.score("test") == 4
    assert project.score("tested") == 61
    assert project.score("stt") == 61

def test_score_blanks():
    player.pull.clear()
    add = ["t", "e", "_", "t" ,"e", "d"]
    player.pull.extend(add)
    player.blanks.append("s")
    assert project.score("test") == 64
    player.blanks.append("x")
    assert project.score("text") == 67
    player.blanks.append("s")
    assert project.score("tested") == 123
    player.blanks.append("x")
    assert project.score("txted") == 123
