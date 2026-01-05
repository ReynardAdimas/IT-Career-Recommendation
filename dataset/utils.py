import pandas as pd

df = pd.read_excel('Job.xlsx')

def enhance_description(row):
    title = row['Job Title']
    skills = row['Required Skills']
    templates = {
    # IT Support & Operations
    "IT Support Specialist": f"Memberikan bantuan teknis dan pemecahan masalah perangkat keras, perangkat lunak, dan sistem untuk memastikan operasional IT berjalan lancar seperti menggunakan {skills}.",
    "IT Support Analyst": f"Menganalisis dan menyelesaikan permasalahan IT yang kompleks, meningkatkan keandalan sistem, serta mendukung pengguna akhir seperti menggunakan {skills}.",
    "IT Helpdesk Support": f"Menjadi titik kontak pertama untuk permasalahan IT dan menyelesaikan kendala teknis dasar seperti menggunakan {skills}.",
    "IT Service Desk Analyst": f"Mengelola permintaan layanan dan tiket insiden serta memastikan kepatuhan terhadap SLA seperti menggunakan {skills}.",
    "System Administrator": f"Menginstal, mengonfigurasi, dan memelihara server serta sistem operasi untuk memastikan ketersediaan sistem  seperti menggunakan {skills}.",
    "Network Administrator": f"Mengelola dan memantau infrastruktur jaringan organisasi untuk memastikan konektivitas dan keamanan seperti menggunakan {skills}.",
    "Network Administrator Trainee": f"Membantu pengelolaan dan pemeliharaan sistem jaringan di bawah pengawasan seperti menggunakan {skills}.",
    "Network Engineer": f"Merancang, mengonfigurasi, memonitor, dan memelihara jaringan LAN, WAN, dan internet untuk mendukung operasional organisasi seperti menggunakan {skills}.",


    # Software Development
    "Software Developer": f"Mengembangkan, menguji, dan memelihara aplikasi perangkat lunak sesuai kebutuhan bisnis menggunakan {skills}.",
    "Software Engineer": f"Merancang, mengembangkan, dan memelihara sistem perangkat lunak yang skalabel dengan praktik rekayasa perangkat lunak menggunakan seperti {skills}.",
    "Full-stack Developer": f"Mengembangkan komponen front-end dan back-end aplikasi, termasuk integrasi database dan API seperti menggunakan {skills}.",
    "Front-end Developer": f"Membangun antarmuka pengguna yang responsif dan interaktif dengan fokus pada pengalaman pengguna  seperti menggunakan {skills}.",
    "Mobile App Developer": f"Merancang dan mengembangkan aplikasi mobile untuk platform Android atau iOS seperti menggunakan {skills}.",
    "UI Developer": f"Mengimplementasikan desain UI/UX menjadi antarmuka yang fungsional dan menarik seperti menggunakan {skills}.",
    "Blockchain Developer": f"Mengembangkan aplikasi terdesentralisasi dan smart contract pada platform blockchain seperti menggunakan {skills}.",
    "Software Architect": f"Menentukan arsitektur sistem dan standar teknis untuk solusi perangkat lunak yang skalabel seperti menggunakan {skills}.",
    "QA Automation Engineer": f"Merancang dan mengimplementasikan framework pengujian otomatis untuk menjamin kualitas perangkat lunak seperti menggunakan {skills}.",
    "Software Tester": f"Menguji aplikasi perangkat lunak untuk menemukan bug dan memastikan fungsionalitas sistem seperti menggunakan {skills}.",
    "Software Development Intern": f"Membantu tugas pengembangan perangkat lunak sambil mempelajari praktik terbaik seperti menggunakan {skills}.",

    # UX / UI
    "UX Designer": f"Merancang pengalaman pengguna yang intuitif melalui riset dan pengujian kegunaan seperti menggunakan {skills}.",
    "UX/UI Designer": f"Merancang pengalaman pengguna dan antarmuka pengguna untuk produk digital seperti menggunakan {skills}.",
    "UX Researcher": f"Melakukan riset pengguna untuk memahami perilaku dan meningkatkan kegunaan produk seperti menggunakan {skills}.",
    "UX Research Assistant": f"Mendukung aktivitas riset UX termasuk pengumpulan dan analisis data seperti menggunakan {skills}.",

    # Data & Analytics
    "Data Analyst": f"Menganalisis dan menginterpretasikan data terstruktur untuk menghasilkan insight dan laporan seperti menggunakan {skills}.",
    "Data Scientist": f"Mengekstraksi insight dari data skala besar menggunakan statistik, machine learning, dan teknik AI dengan seperti {skills}.",
    "Data Engineer": f"Membangun dan memelihara pipeline serta infrastruktur data untuk mendukung analitik seperti menggunakan {skills}.",
    "Database Administrator": f"Mengelola sistem basis data untuk memastikan performa, keamanan, dan ketersediaan seperti menggunakan {skills}.",
    "Database Analyst": f"Menganalisis struktur database dan mengoptimalkan penggunaan data seperti menggunakan {skills}.",
    "Data Analytics Manager": f"Memimpin tim dan strategi analitik data untuk mendukung pengambilan keputusan berbasis data seperti menggunakan {skills}.",
    "Data Governance Analyst": f"Memastikan kualitas data, kepatuhan, dan tata kelola data seperti menggunakan {skills}.",
    "Data Analyst Intern": f"Membantu proses analisis data dan pembuatan laporan di bawah bimbingan seperti menggunakan {skills}.",

    # AI & ML
    "AI/ML Engineer": f"Merancang dan menerapkan model kecerdasan buatan dan machine learning ke lingkungan produksi seperti menggunakan {skills}.",
    "Machine Learning Engineer": f"Mengembangkan, mengoptimalkan, dan memelihara pipeline serta model machine learning seperti menggunakan {skills}.",
    "AI Ethics Consultant": f"Memastikan penggunaan teknologi AI yang etis, adil, dan bertanggung jawab seperti menggunakan {skills}.",

    # Cloud & DevOps
    "Cloud Architect": f"Merancang arsitektur berbasis cloud yang skalabel dan aman seperti menggunakan {skills}.",
    "Cloud Solutions Architect": f"Mengembangkan solusi cloud yang selaras dengan kebutuhan bisnis seperti menggunakan {skills}.",
    "Cloud Solutions Analyst": f"Menganalisis dan merekomendasikan layanan serta arsitektur cloud seperti menggunakan {skills}.",
    "Cloud Support Engineer": f"Memberikan dukungan teknis dan operasional untuk lingkungan cloud seperti menggunakan {skills}.",
    "Cloud Security Engineer": f"Mengimplementasikan kontrol dan kebijakan keamanan pada infrastruktur cloud seperti menggunakan {skills}.",
    "Cloud Security Analyst": f"Memonitor dan menganalisis risiko keamanan pada lingkungan cloud seperti menggunakan {skills}.",
    "Cloud Migration Specialist": f"Merencanakan dan mengeksekusi migrasi sistem ke platform cloud seperti menggunakan {skills}.",
    "Cloud Solutions Intern": f"Mendukung perancangan dan implementasi solusi cloud seperti menggunakan {skills}.",
    "DevOps Engineer": f"Mengotomatiskan dan mengoptimalkan pipeline CI/CD serta infrastruktur seperti menggunakan {skills}.",
    "DevSecOps Engineer": f"Mengintegrasikan praktik keamanan ke dalam pipeline DevOps seperti menggunakan {skills}.",

    # Cybersecurity & Risk
    "Cybersecurity Analyst": f"Memonitor sistem dan jaringan untuk mendeteksi serta mencegah ancaman keamanan seperti menggunakan {skills}.",
    "Cybersecurity Engineer": f"Merancang dan mengimplementasikan sistem serta mekanisme pertahanan keamanan seperti menggunakan {skills}.",
    "IT Security Analyst": f"Menganalisis kerentanan dan memastikan perlindungan aset IT seperti menggunakan {skills}.",
    "IT Security Consultant": f"Memberikan konsultasi strategi dan implementasi keamanan IT seperti menggunakan {skills}.",
    "Network Security Engineer": f"Mengamankan infrastruktur jaringan dari ancaman siber seperti menggunakan {skills}.",
    "IT Risk Analyst": f"Mengidentifikasi dan mengelola risiko IT terhadap operasional bisnis seperti menggunakan {skills}.",
    "IT Auditor": f"Melakukan audit sistem dan proses IT untuk memastikan kontrol dan kepatuhan seperti menggunakan {skills}.",
    "IT Compliance Officer": f"Memastikan operasional IT sesuai dengan regulasi dan kebijakan yang berlaku seperti menggunakan {skills}.",
    "IT Compliance Specialist": f"Mengimplementasikan dan memantau kerangka kerja kepatuhan IT seperti menggunakan {skills}.",
    "Data Privacy Officer": f"Memastikan perlindungan dan penggunaan data pribadi secara sah seperti menggunakan {skills}.",

    # Management & Governance
    "IT Project Manager": f"Merencanakan dan mengelola proyek IT agar selesai tepat waktu dan sesuai target seperti menggunakan {skills}.",
    "IT Project Coordinator": f"Mendukung pelaksanaan proyek melalui koordinasi dan dokumentasi seperti menggunakan {skills}.",
    "IT Change Manager": f"Mengelola perubahan sistem IT untuk meminimalkan gangguan bisnis seperti menggunakan {skills}.",
    "IT Business Analyst": f"Menjembatani kebutuhan bisnis dan solusi IT melalui analisis dan dokumentasi seperti menggunakan {skills}.",
    "Business Analyst": f"Menganalisis proses bisnis dan merekomendasikan perbaikan seperti menggunakan {skills}.",
    "IT Governance Manager": f"Menyusun tata kelola IT dan menyelaraskan strategi IT dengan tujuan organisasi seperti menggunakan {skills}.",
    "IT Business Continuity Manager": f"Menjamin keberlangsungan layanan IT saat terjadi gangguan seperti menggunakan {skills}.",
    "IT Asset Manager": f"Mengelola siklus hidup dan pemanfaatan aset IT seperti menggunakan {skills}.",
    "IT Analyst": f"Menganalisis sistem IT dan mendukung proses pengambilan keputusan seperti menggunakan {skills}.",
    "IT Analyst Trainee": f"Belajar dan membantu analisis sistem serta dukungan IT seperti menggunakan {skills}.",

    # Procurement & Sales
    "IT Procurement Manager": f"Mengelola strategi pengadaan IT dan hubungan dengan vendor seperti menggunakan {skills}.",
    "IT Procurement Specialist": f"Menangani proses pengadaan barang dan jasa IT secara efisien seperti menggunakan {skills}.",
    "IT Procurement Analyst": f"Menganalisis kebutuhan dan biaya pengadaan IT seperti menggunakan {skills}.",
    "IT Procurement Coordinator": f"Mengoordinasikan proses dan dokumentasi pengadaan IT seperti menggunakan {skills}.",
    "IT Sales Manager": f"Memimpin strategi penjualan produk dan layanan IT seperti menggunakan {skills}.",
    "IT Sales Representative": f"Menjual solusi IT dan menjaga hubungan dengan pelanggan seperti menggunakan {skills}.",

    # Training & Consulting
    "IT Trainer": f"Menyelenggarakan pelatihan untuk meningkatkan keterampilan teknis seperti menggunakan {skills}.",
    "IT Trainer Assistant": f"Mendukung pelaksanaan pelatihan IT dan persiapan materi seperti menggunakan {skills}.",
    "IT Trainer Specialist": f"Memberikan pelatihan IT yang bersifat spesialis pada teknologi tertentu seperti menggunakan {skills}.",
    "IT Consultant": f"Memberikan rekomendasi dan solusi strategis IT bagi organisasi seperti menggunakan {skills}.", 
    "IT Quality Analyst": f"Menganalisis, menguji, dan mengevaluasi sistem serta proses IT untuk memastikan kualitas, kepatuhan, dan keandalan layanan menggunakan {skills}."
    }

    if title in templates:
        return templates[title]

df['Job Description'] = df.apply(enhance_description, axis=1)
print(df[['Job Title', 'Job Description']].head())
df.to_csv('Job_New.csv', index=False)