conv = (
    (
        r"I have a question ?",
        ("Please ask, I can answers your question regarding the site or the course / contents we provide.",)
    ),
    (
        r"how is the college infrastructure|how (.*) infrastructure",
        ("our infrastructure consist of canteen, hostel, premises, tranport facility, central computing facility, and office",)
    ),
    (
        r"what is the address of college|what is the exact location of college|(.*) location of college",
        ("A1 Sector 7, Gida, Gorakhpur",)
    ),
    (
        r"exactly how far is college from station ?|(.*)college from station",
        ("Approximatly 30-45 minutes by bus or riksha",)
    ),
    (
        r"what are the means of transport ?|(.*) transport (.*)",
        ("By riksha or by bus",)
    ),
    (
        r"how is the hostel facility ?|(.*) hostel facility",
        ("We can accomodate upto 250 students",)
    ),
    (
        r"can you please provide me the contact details|(.*) contact details|(.*) phone no",
        ("Yes sure, Phone No. : 123456789",)
    ),

    (
        r"what is the timing of college ?|(.*)college timing",
        ("From Morning 9 am to 4:20 pm, and it varies according to your batch in which you are enrolled.",)
    ),
    (
        r"when does the college library opens ?|(.*)college library",
        ("It opens at 9 am in morning",)
    ),
    (
        r"what is the working time of office ?|(.*) time of office",
        ("Between 10 am - 5 pm",)
    ),

    (
        r"what is the fees structure ?| (.*) fees structure",
        ("Fee structure will be available to you in our office.",)
    ),
    (
        r"what is the institute code of ITM ?|(.*) institute code",
        ("120 is the institute code of our college.",)
    ),
    (
        r"is ITM affiliated wih AKTU? | (.*) AKTU (.*)",
        ("Yes, college has been affiliated wih AKTU.",)
    ),
    (
        r"what are the placement opportunity in ITM ?| (.*) placement (.*)",
        ("https://ITM.edu.in/placement-summary/ This is the ITM placement record.",)
    ),
    (
        r"(.*) companies comes for campus interview ?|(.*) companies (.*)",
        ("Yes",)
    ),
    (
        r"can you provide me the academic calander of 2022-2023| (.*) academic calander",
        ("Yes, https://ITM.edu.in/wp-content/uploads/2022/07/Academic-Calendar-2022-23-odd.pdf",)
    ),
    (
        r"do you have any website|(.*) website",
        ("Yes, Here it is https://ITM.edu.in/",)
    ),
    (
        r"what is the name of Director of ITM college ?| (.*) name of Director ",
        ("Dr. N K SINGH",)
    ),
    (
        r"what is the name of hod of CSE department ?| (.*) hod of cse department| (.*) hod of cse dep",
        ("Prof. ASHUTOSH KUMAR RAO",)
    ),

    (
        r"(.*) ITM| (.*) itm gida",
        ("Institute of Technology and Management Gorakhpur",)
    ),
    (
        r"what is the name of class coordinator",
        ("Mr. ",)
    ),
    (
        r"who is your creator",
        ("Rohit Kumar",)
    ),
    (
        r"how many department (.*)| (.*) many department (.*)",
        ("6, Computer Science, AI/ML, Data Science, Civil Engineering and Electronic & Communications, and Mechanical.",)
    ),
    (
        r"how many labs are there in cse department ?| (.*) labs in cse department",
        ("5, computer network lab (01), database lab (02), analysis and design lab (03), signal and image processing lab (04), open source lab (05).",)
    ),
    (
        r"where can i find result (.*)| (.*) find result (.*)",
        ("https://erp.aktu.ac.in/WebPages/OneView/OneView.aspx",)
    ),
    (
        r"where can i find syllabus (.*) | (.*) find syllabus (.*)",
        ("https://aktu.ac.in/",)
    ),
    (
        r"where can i find previous year question papers ?| (.*) question paper",
        ("https://aktu.ac.in/",)
    ),
    (
        r"hi|hey|hello",
        ("Hello, How can I help you!",)
    ),
    (
        r"hi, I am Rohit.",
        ("Hello, Rohit can I help you!",)
    ),
    (
        r"my name is (.*)",
        ("Hello, %1 How are you today ?",)
    ),
    (
        r"what is your name ?",
        ("My name is Chatbot",)
    ),
    (
        r"who are you ?",
        ("i am Chatbot. I try to answer questions, Sometimes i get them right. Sometimes i need additional help. I am designed to get better overtime. How can i help you ?",)
    ),
    (
        r"how are you ?",
        ("I'm doing good, How about You ?",)
    ),
    (
        r"sorry (.*)|sorry",
        ("Its alright","Its OK, never mind",)
    ),
    (
        r"i'm (.*) doing good",
        ("Nice to hear that","Alright :)",)
    ),
    (
        r"(.*) create you ?",
        ("Rohit Kumar created me using Python's NLTK library",)
    ),
    (
        r"how is weather in (.*)?",
        ("Weather in %1 is awesome like always",)
    ),

    (
        r"i study in (.*)?",
        ("%1 is  Good , I have heard about it.",)
    ),
    (
        r"who made you",
        ("Rohit Kumar",)
    ),(
        r"who is radha",
        ("Radha is a Best friend of Rohit",)
    ),
    (
        r"what is the name of project coordinator",
        ("Mr. Nitin Dixit",)
    ),
    (
        r"good",
        ("thank you",)
    ),
    (
        r"bye|quit",
        ("Bye take care. See you soon","It was nice talking to you. See you soon")
    ),
)