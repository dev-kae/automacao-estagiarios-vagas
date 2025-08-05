from model import Site, Plataform

sites = [
    Site(
        url="https://www.glassdoor.com.br/Vaga/s%C3%A3o-paulo-s%C3%A3o-paulo-brasil-backend-junior-vagas-SRCH_IL.0,26_IC2479061_KO27,41.htm",
        plataform=Plataform.GLASSDOOR,
    ),
    Site(
        url="https://www.linkedin.com/jobs/search/?currentJobId=4096466261&f_AL=true&f_E=2&geoId=92000000&keywords=backend%20junior&location=Brasil",
        plataform=Plataform.LINKEDIN,
    )
]

