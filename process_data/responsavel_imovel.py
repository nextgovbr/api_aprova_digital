from utilities.my_tools import b_resp

def _build_address_respo(respo):
    '''Build address info by parsing address related keys'''

    endereco = [respo.get_m(['rua_proprietario'], None),
                respo.get_m(['numero_proprietario'], None),
                respo.get_m(['complemento_prop'], None),
                respo.get_m(['bairro_proprietario'], None),
                respo.get_m(['cidade_proprietario'], None),
                respo.get_m(['uf-proprietario'], None)
                ]
    endereco = [item for item in endereco if item is not None]

    if not endereco:
        return None

    endereco = ', '.join(endereco)

    return endereco


def _dados_um_resp(respo):
    '''Parse all the data for one of the owner's info'''

    dados = [
        b_resp(
            'nome',
            'Nome do responsável pelo imóvel',
            respo.get_m(['nome-proprietario'], None)),
        b_resp(
            'tipo_vinculo',
            'Tipo de vínculo do responsável pelo imóvel',
            respo.get_m(['tipo_vinculo_proprietario',
                         'tipo_vinculo'], None)),

        b_resp(
            'doc',
            'Número do documento do responsável pelo imóvel',
            respo.get_m(['cpfcnpj_proprietario']).get_m(['cpfCnpj'], None)),

        b_resp(
            'tipo_doc',
            'Tipo de documento do responsável pelo imóvel',
            respo.get_m(['cpfcnpj_proprietario']).get_m(['type'], None)),

        b_resp(
            'email',
            'E-mail do responsável pelo imóvel',
            respo.get_m(['email_proprietario'], None)),

        b_resp(
            'endereco',
            'Endereço do responsável pelo imóvel',
            _build_address_respo(respo)),

        b_resp('cep',
               'CEP do responsável pelo imóvel',
               respo.get_m(['cep_proprietario'], None)),

        #NÃO CONSEGUI IDENTIFICAR NENHUM PROCESSO COM INFORMAÇÃO DE TELEFONE DO RESP
        b_resp('telefone',
               'Telefone do responsável pelo imóvel',
               'Informação Não Disponível'))
    ]

    return dados


def dados_resps_imovel(proc):
    '''Get's info for all building owners'''

    resps_imovel = proc.get_m(['last_version']) \
        .get_m(['proprietario'], [])

    dados_resps = []
    for respo in resps_imovel:
        dados_resps.append(_dados_um_resp(respo))

    return dados_resps