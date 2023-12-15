from flask_nav import Nav
from flask_nav.elements import Navbar, View, Subgroup


def create_nav(app):
    nav = Nav()
    nav.init_app(app)

    @nav.navigation()
    def menu_navbar():
        menu = Navbar('HSC')
        menu.items = [View('Home', 'home.home'),
                      Subgroup(
                          'Cadastros',
                          View('Meus Dados', 'home.home'),
                          View('Exames', 'home.home'),
                          View('Meus Médicos', 'home.home')
                      ),
                      Subgroup(
                          'Visualizar Exames',
                          View('RX', 'home.home'),
                          # View('Ressonância Magnética', 'exam.manage_rx'),
                      )
                      ]

        menu.items.append(View('Sair', 'home.home'))
        return menu

    @nav.navigation()
    def menu_doctor():
        menu = Navbar('HSC')
        menu.items = [View('Home', 'auth.login_doctor'),
                      View('Visualizar Exames', 'doctor.doctor_view')
                      ]
        menu.items.append(View('Sair', 'auth.logout'))
        return menu
