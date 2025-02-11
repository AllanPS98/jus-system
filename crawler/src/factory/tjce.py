from bs4 import BeautifulSoup
from src.config import ApplicationConfig
from src.factory.court import Court

config_app = ApplicationConfig()

class Tjce(Court):
    name = 'tjce'

    def __get_process_class(self):
        process_class = self.soup.find('span', {'id': 'classeProcesso'})
        if process_class:
            return process_class.text.strip()

    def __get_area(self):
        div_ = self.soup.find('div', {'id': 'areaProcesso'})
        if div_:
            return div_.find('span').text.strip()

    def __get_subject(self):
        subject = self.soup.find('span', {'id': 'assuntoProcesso'})
        if subject:
            return subject.text.strip()
    
    def __get_distribution_date(self):
        distribution_date = self.soup.find('div', {'id': 'dataHoraDistribuicaoProcesso'})
        if distribution_date:
            return distribution_date.text.strip()
    
    def __get_judge(self):
        judge = self.soup.find('span', {'id': 'juizProcesso'})
        if judge:
            return judge.text.strip()
    
    def __get_share_value(self):
        share_value = self.soup.find('div', {'id': 'valorAcaoProcesso'})
        if share_value:
            return share_value.text.replace(' ', '').strip()
    
    def __get_parts(self):
        all_parts = self.soup.find('table', {'id': 'tableTodasPartes'})
        main_parts = self.soup.find('table', {'id': 'tablePartesPrincipais'})
        table_ = all_parts if all_parts else main_parts
        if table_:
            rows = table_.find_all('tr')
            parts = []
            for row in rows:
                part = {}
                participation_type = row.find('span', {'class': 'mensagemExibindo tipoDeParticipacao'})
                key = participation_type.text.replace('\xa0', '')
                table_data = row.find('td', {'class': 'nomeParteEAdvogado'})
                part_text = table_data.text.replace('\n', '').replace('\t', '').replace('\xa0', ' ')
                part_text_splitted = part_text.split(':')
                part_name = part_text_splitted[0]
                part_name = ' '.join(part_name.split(' ')[:-1])
                lawyers = []
                type_lawyer = part_text_splitted[0].split(' ')[-1]
                for part_text in part_text_splitted[1:]:
                    part_text_splitted_2 = part_text.split(' ')
                    dict_lawyer = {type_lawyer: ' '.join(part_text_splitted_2[:-1]).strip()}
                    lawyers.append(dict_lawyer)
                    type_lawyer = part_text_splitted_2[-1]
                part_dict = {'name': part_name.strip(), 'lawyers': lawyers}
                part[key] = part_dict
                parts.append(part)
            return parts
    
    def __get_moves(self):
        table_ = self.soup.find('tbody', {'id': 'tabelaTodasMovimentacoes'})
        if table_:
            rows = table_.find_all('tr')
            moves = []
            for row in rows:
                move = {
                    'date': row.find('td', {'class': 'dataMovimentacao'}).text.strip(),
                    'description': row.find('td', {'class': 'descricaoMovimentacao'}).text.strip(),
                }
                moves.append(move)
            return moves

    def __get_process_class_sd(self):
        div_ = self.soup.find('div', {'id': 'classeProcesso'})
        if div_:
            span_ = div_.find('span').text.strip()
            return span_

    def __get_area_sd(self):
        div_ = self.soup.find('div', {'id': 'areaProcesso'})
        if div_:
            return div_.find('span').text.strip()
    
    def __get_subject_sd(self):
        div_ = self.soup.find('div', {'id': 'assuntoProcesso'})
        if div_:
            return div_.find('span').text.strip()
    
    def __get_parts_sd(self):
        all_parts = self.soup.find('table', {'id': 'tableTodasPartes'})
        main_parts = self.soup.find('table', {'id': 'tablePartesPrincipais'})
        table_ = all_parts if all_parts else main_parts
        if table_:
            rows = table_.find_all('tr')
            parts = []
            for row in rows:
                part = {}
                key, part_text_splitted, part_name = self.__get_part_name_values(row)
                lawyers = self.__get_lawyers(part_text_splitted)
                part_dict = {'name': part_name, 'lawyers': lawyers}
                part[key] = part_dict
                parts.append(part)
            return parts

    def __get_lawyers(self, part_text_splitted):
        lawyers = []
        type_lawyer = part_text_splitted[0].split(' ')[-1]
        for part_text in part_text_splitted[1:]:
            part_text_splitted_2 = part_text.split(' ')
            dict_lawyer = {type_lawyer: ' '.join(part_text_splitted_2[:-1]).strip()}
            lawyers.append(dict_lawyer)
            type_lawyer = part_text_splitted_2[-1]
        return lawyers

    def __get_part_name_values(self, row):
        participation_type = row.find('span', {'class': 'mensagemExibindo tipoDeParticipacao'})
        key = participation_type.text.replace('\xa0', '')
        table_data = row.find('td', {'class': 'nomeParteEAdvogado'})
        part_text = table_data.text.replace('\n', '').replace('\t', '').replace('\xa0', ' ')
        part_text_splitted = part_text.split(':')
        part_name = part_text_splitted[0]
        part_name = ' '.join(part_name.split(' ')[:-1]).strip()
        return key, part_text_splitted, part_name
    
    def __get_moves_sd(self):
        table_ = self.soup.find('tbody', {'id': 'tabelaTodasMovimentacoes'})
        if table_:
            rows = table_.find_all('tr')
            moves = []
            for row in rows:
                move = {
                    'date': row.find('td', {'class': 'dataMovimentacaoProcesso'}).text.strip(),
                    'description': row.find('td', {'class': 'descricaoMovimentacaoProcesso'}).text.strip(),
                }
                moves.append(move)
            return moves
    
    def __check_not_found(self):
        get_message = self.soup.find('td', {'id': 'mensagemRetorno'})
        if get_message and "Não existem informações disponíveis para os parâmetros informados." in get_message.find('li').text:
            return True
        return False
    
    def __get_first_degree(self, process_number):
        url = config_app.TJCE_URL_SEARCH_FIRST_DEGREE
        params = f'''?conversationId=&cbPesquisa=NUMPROC&numeroDigitoAnoUnificado={".".join(process_number.split('.')[:2])}&foroNumeroUnificado={process_number.split('.')[-1]}&dadosConsulta.valorConsultaNuUnificado={process_number}&dadosConsulta.valorConsultaNuUnificado=UNIFICADO&dadosConsulta.valorConsulta=&dadosConsulta.tipoNuProcesso=UNIFICADO'''
        response = self.session.get(
            url=url + params
        )
        html_result = response.text
        self.soup = BeautifulSoup(html_result, 'html.parser')
        if self.__check_not_found():
            return
        process_data = {
            'court_name': self.name,
            'process_number': process_number,
            'degree': 1,
            'process_class': self.__get_process_class(),
            'area': self.__get_area(),
            'subject': self.__get_subject(),
            'distribution_date': self.__get_distribution_date(),
            'judge': self.__get_judge(),
            'share_value': self.__get_share_value(),
            'parts': self.__get_parts(),
            'moves': self.__get_moves(),
        }
        return process_data
    
    def __get_second_degree(self, process_number):
        url = config_app.TJCE_URL_SEARCH_SECOND_DEGREE
        params = f'''?conversationId=&paginaConsulta=0&cbPesquisa=NUMPROC&numeroDigitoAnoUnificado={".".join(process_number.split('.')[:2])}&foroNumeroUnificado={process_number.split('.')[-1]}&dePesquisaNuUnificado={process_number}&dePesquisaNuUnificado=UNIFICADO&dePesquisa=&tipoNuProcesso=UNIFICADO'''
        response = self.session.get(
            url=url + params
        )
        html_result = response.text
        self.soup = BeautifulSoup(html_result, 'html.parser')
        if self.__check_not_found():
            return
        input_process_code = self.soup.find('input', {'id': 'processoSelecionado'})
        if input_process_code:
            process_data_sd = self.__get_process_with_input(process_number, input_process_code)
            return [process_data_sd]
        div_list_process = self.soup.find('div', {'id': 'listagemDeProcessos'})
        if div_list_process:
            results = self.__get_sd_process_with_more_than_one(process_number, div_list_process)
            return results
        process_data_sd = {
            'court_name': self.name,
            'process_number': process_number,
            'degree': 2,
            'process_class': self.__get_process_class_sd(),
            'area': self.__get_area_sd(),
            'subject': self.__get_subject_sd(),
            'distribution_date': self.__get_distribution_date(),
            'judge': self.__get_judge(),
            'share_value': self.__get_share_value(),
            'parts': self.__get_parts_sd(),
            'moves': self.__get_moves_sd(),
        }
        return [process_data_sd]
    
    def __get_process_with_input(self, process_number, input_process_code):
        process_code = input_process_code.get('value')
        url = config_app.TJCE_URL_SHOW_SECOND_DEGREE
        params = f'''?processo.codigo={process_code}'''
        response = self.session.get(
            url=url + params
        )
        html_result = response.text
        self.soup = BeautifulSoup(html_result, 'html.parser')
        process_data_sd = {
            'court_name': self.name,
            'process_number': process_number,
            'degree': 2,
            'process_class': self.__get_process_class_sd(),
            'area': self.__get_area_sd(),
            'subject': self.__get_subject_sd(),
            'distribution_date': self.__get_distribution_date(),
            'judge': self.__get_judge(),
            'share_value': self.__get_share_value(),
            'parts': self.__get_parts_sd(),
            'moves': self.__get_moves_sd(),
        }
        
        return process_data_sd

    def __get_sd_process_with_more_than_one(self, process_number, div_list_process):
        lis_ = div_list_process.find_all('li')
        hrefs = []
        for item in lis_:
            a_ = item.find('a', {'class': 'linkProcesso'})
            distribution_date = item.find('div', {'class': 'dataLocalDistribuicao'}).text
            if a_:
                data = {
                    'link': a_['href'],
                    'distribution_date': distribution_date
                }
                hrefs.append(data)
        results = []
        base_url = config_app.TJCE_URL_FIRST_DEGREE.split('/cpopg')[0]
        for href in hrefs:
            response = self.session.get(url=base_url + href['link'])
            html_result = response.text
            self.soup = BeautifulSoup(html_result, 'html.parser')
            process_data_sd = {
                'court_name': self.name,
                'process_number': process_number,
                'degree': 2,
                'process_class': self.__get_process_class_sd(),
                'area': self.__get_area_sd(),
                'subject': self.__get_subject_sd(),
                'distribution_date': href['distribution_date'],
                'judge': self.__get_judge(),
                'share_value': self.__get_share_value(),
                'parts': self.__get_parts_sd(),
                'moves': self.__get_moves_sd(),
            }
            results.append(process_data_sd)
        return results

    def get_process(self, process_number: str):
        process_data = self.__get_first_degree(process_number)
        process_data_sd = self.__get_second_degree(process_number)
        results = []
        if process_data:
            results.append(process_data)
        if process_data_sd:
            results.extend(process_data_sd)
        return results
