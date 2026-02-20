def test_criar_estudante(client):
    response = client.post(
        "/estudantes/",
        json={"nome": "João", "idade": 21}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["nome"] == "João"
    assert "id" in data


def test_atualizar_estudante(client):
    response = client.put(
        "/estudantes/1",
        json={"nome": "João Atualizado", "idade": 22}
    )
    assert response.status_code == 200
    assert response.json()["nome"] == "João Atualizado"


def test_deletar_estudante(client):
    response = client.delete("/estudantes/1")
    assert response.status_code == 200
