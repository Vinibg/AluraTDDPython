from operator import le
from unittest import TestCase
from src.leilao.dominio import Usuario, Lance, Leilao

class TesteLeilao(TestCase):

    def setUp(self):
        self.gui = Usuario("gui",500.0)
        self.lance_gui = Lance(self.gui, 150.0)
        self.leilao = Leilao("Celular")
        
        
    def test_deve_retornar_o_maior_e_o_menor_em_order_crescente(self):
        yuri = Usuario("yuri",500.0)
        lance_yuri = Lance(yuri, 100.0)

        self.leilao.propoe(lance_yuri)
        self.leilao.propoe(self.lance_gui)


        menor_valor_esperado = 100
        maior_valor_esperado = 150

        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)      
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)      

    def test_nao_deve_permitir_propor_um_lance_em_ordem_decrescente(self):
        
        with self.assertRaises(ValueError):
            yuri = Usuario("yuri",500.0)

            lance_yuri = Lance(yuri, 100.0)

            self.leilao.propoe(self.lance_gui)
            self.leilao.propoe(lance_yuri)


    def test_deve_retornar_o_mesmo_valor_para_o_maior_e_menor_lance(self):
        
        self.leilao.propoe(self.lance_gui)
              
        self.assertEqual(150.0, self.leilao.menor_lance)
        self.assertEqual(150.0, self.leilao.maior_lance)

    def test_deve_retornar_o_maior_e_menor_quando_o_leilao_tiver_tres_lances(self):
        vini = Usuario("vini",500.0)
        yuri = Usuario("yuri",500.0)
        lance_yuri = Lance(yuri, 100.0)
        lance_vini = Lance(vini,200.0)


        self.leilao.propoe(lance_yuri)
        self.leilao.propoe(self.lance_gui)
        self.leilao.propoe(lance_vini)
 
        menor_valor_esperado = 100
        maior_valor_esperado = 200
        
        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)      
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance) 
        
    
    #se leilao não tiver lance, deve permitir propor lance
    def test_deve_permitir_propor_lance_caso_o_leilao_nao_tenha_lances(self):
        self.leilao.propoe(self.lance_gui)
        
        quatindade_de_lance_recebido = len(self.leilao.lances)

        self.assertEqual(1, quatindade_de_lance_recebido)

    #se ultimo usuario for diferente, deve permitir propor lance
    def test_deve_permitir_propor_o_lance_caso_o_ultimo_usuario_seja_diferente(self):
        yuri = Usuario("Yuri",500.0)
        lance_do_yuri = Lance(yuri, 200.0)
        
        self.leilao.propoe(self.lance_gui)
        self.leilao.propoe(lance_do_yuri)
        
        quantidade_de_lances = len(self.leilao.lances)
        self.assertEqual(2, quantidade_de_lances)

    #se ultimo usuario for o mesmo, não deve permitir lance

    def test_nao_deve_permitir_propor_lance_se_usuario_for_o_mesmo(self):
        lance_2 = Lance(self.gui, 200.0)
        
        with self.assertRaises(ValueError):
            self.leilao.propoe(self.lance_gui)
            self.leilao.propoe(lance_2)