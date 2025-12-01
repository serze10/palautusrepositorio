Github copilot antoi minulle kaksi kritiikkiä. 

Ensimmäinen liittyi siihen, että normal_score() nostaisi KeyErrorin kun pisteet nousisivat 3 yli mutta tässä kuitenkin get_score() ohjaa kaikki tilanteet, joissa pisteet ≥ 4, suoraan endgame_score()‑metodiin. Tämä estää virheen normaalisti. 
Copilotin huomio: normal_score() ei ole itsenäisesti turvallinen se luottaa siihen, että get_score() ei koskaan kutsu sitä väärässä tilanteessa. Jos joku muu kutsuisi normal_score() suoraan, se voisi kaatua.
Ehdotettu korjaus:
if player1_score > 3 or player2_score > 3:
    raise ValueError("normal_score() called with invalid score") 

Toinen kritiikki liittyi tie_score() metodiin. Kun pisteet ovat tasan, metodi hakee SCORE_NAMES[player1_score].

Jos player1_score ≥ 3, pitäisi palauttaa "Deuce". Tämä on jo huomioitu, mutta vain täsmälleen 3:lle.
Jos molemmilla on ≥ 4, metodi yrittäisi hakea SCORE_NAMES[4], ei löydy ja KeyError.
Nykyinen logiikka: get_score() estää tämän, koska se ei kutsu tie_score() kun pisteet ovat ≥ 4.
Copilotin huomio: Metodi ei ole itsenäisesti turvallinen – se kaatuisi jos sitä kutsutaan väärässä tilanteessa.
Ehdotettu korjaus:
if player1_score >= 3:
    return "Deuce"
return f"{SCORE_NAMES[player1_score]}-All"