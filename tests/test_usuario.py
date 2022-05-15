from src.leilao.dominio import Usuario, Leilao
import pytest

@pytest.fixture
def vini():
    return Usuario("vini", 100)

@pytest.fixture
def leilao():
    return Leilao("Geladeira")

def test_deve_subtrair_valor_da_carteira_do_usuario_apos_um_lance(vini, leilao):

    vini.propoe_lance(leilao, 50.0)

    assert vini.carteira == 50.0

def test_deve_permanecer_o_mesmo_se_o_valor_for_igual_a_zero(vini, leilao):

    vini.propoe_lance(leilao, 0.0)

    assert vini.carteira == 100.0

def test_deve_dimunir_a_carteira_com_o_valor_menor_do_que_ha_na_carteira(vini, leilao):

    vini.propoe_lance(leilao, 1.0)

    assert vini.carteira == 99.0

def test_nao_deve_aceitar_valor_maior_que_a_carteira(vini, leilao):
    with pytest.raises(ValueError):

        vini.propoe_lance(leilao, 200.0)