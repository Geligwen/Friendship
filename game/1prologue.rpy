#prolougue#
label prologue:
    label prologueday1:
        play ambience ambiencenight fadein 60.0
        play music hopelessness
        if persistent.skip == 1:
            menu:
                "Хотите ли вы пропустить пролог? Не рекомендуется, если Вы играете первый раз"
                "Да":
                    menu:
                        "Вы уверены?"
                        "Да, пропустить пролог":
                            python:
                                playername = renpy.input("Как вас зовут?")
                                playername = playername.strip()
                                if not playername:
                                    playername = "Антон"
                            jump morning
                        "Нет, я хочу посмотреть начало истории!":
                            pass
                "Нет":
                    pass
        $ persistent.skip = 1
        scene bg moxiewagoncandles with s
        unknown "Хорошо... Попытаюсь в третий раз..."
        unknown "Призыв... Фамильяра!!"
        play sound thunder1
        scene bg purple with dissolve
        scene bg black with dissolve
        "Сноп искр ударяет меня,толчками распространяясь по каждому нервному окончанию, внезапно наполняя меня мучительным осознанием."
        "Несмотря на навалившуюся вялость и сонливость, я умудряюсь устоять на ногах, и даже чувствую себя на удивление спокойно."
        "Все, что я вижу, - это бесконечня, простирающаяся во все стороны, чернота, сопровождаемая жуткой тишиной."
        "Тишина... Но вдруг я слышу незнакомый голос, пробивающийся сквозь темноту..."
        unknown "*кхе, кхе* тьфу... Черт возьми, свечи погасли? Что происходит?"
        unknown "Да будет свет!"
        scene bg blackpurpleglow with dissolve
        "После этих слова в нескольких футах впереди того места, где я стою, загорается тусклый фиолетовый огонек."
        "С моим плохим зрением трудно что-то разглядеть, но вскоре я начинаю различать чей-то синий силуэт."
        show moxie silhouettehappy with s
        "Человек? Нет... Он выглядит как гуманоид, но слишком темно, чтобы ясно разглядеть его."
        unknown "Невероятно! Это заклинание действительно сработало! Наконец-то я вызвала мужчину-фамильяра."
        show moxie silhouettelaughing with dissolve
        unknown "Ха, конечно оно сработало! Хах, потрясающе!"
        "У этого таинственного силуэта был женский голос, и по какой-то причине она была в экстазе."
        "Не сумев сдержать своего волнения, она подпрыгнула ко мне, наклоняясь, чтобы поближе рассмотреть меня, что позволило мне хорошенько разглядеть ее."
        show moxie closesilhouettehappyneutral with dissolve
        "Она выглядела как голубое гуманоидное существо, напоминающее антропоморфную лошадь или пони. Она была полностью обнажена, сквозь блестящий мех на её груди выступали соски с розоватыми ареолами вокруг."
        show moxie closesilhouetteshocked with dissolve
        unknown "Ох, хм... Какого черта? Может быть, я ошиблась с заклинанием... Что за странный пони без шерсти, нет... Это вовсе не пони."
        show moxie closesilhouettehorny with dissolve
        unknown "Ну и ладно! Не имеет значения, что это за вид, мой новый раб симпатичный!"
        unknown "Прекрасно! Хорошо, раб, ты можешь выполнять приказы?"
        unnamedmc "Хм... Что происходит?"
        show moxie silhouetteembarrassed with dissolve
        stop music fadeout 30.0
        "Я слегка наклоняюсь к ней, но она отшатывается с широко раскрытыми глазами; она так потрясена, как будто только что увидела паука, ползущего по мне."
        show moxie silhouetteserious with dissolve
        unknown "Т-ты умеешь говорить! Ты не должен этого делать! Плохой раб!"
        unnamedmc "О чем ты говоришь? Конечно, я могу говорить..."
        show moxie silhouettesad with dissolve
        unknown "О... Но в книге заклинаний сказано, что это невозможно!"
        unknown "Теперь действительно ничего не понятно!"
        unnamedmc "Поверь мне, я в таком же замешательстве, как и ты."
        "Слабость такая сильная, что я едва могу понять, что происходит."
        menu:
            "Это может быть сон, но он кажется слишком реальным."
            "Ты что, пони?":
                unknown "Ну, вообще-то, единорог..."
            "Ты только что сказала \"книга заклинаний\"?":
                unknown "Да, я только что произнесла заклинание и ... .."
        unknown "Погоди, это я должна задавать вопросы!"
        unnamedmc "Но я понятия не имею, что происходит, а ты только что назвала меня рабом!"
        show moxie silhouetteserious with dissolve
        unknown "Ладно, хорошо... Я Мо-... Мокси"
        moxie "Ты в моем доме, в моем фургоне, в городе Аркадия."
        "Я в фургоне? Я шевелю пальцами ног и чувствую, что стою на деревянном полу."
        "Когда я начал осматривать темную комнату, в воздухе разлился восхитительно мягкий запах лаванды"
        "Всё, что я чувствую, и всё, что я испытываю внутри себя вплоть до самых мельчайших деталей, явно не похоже на сон, это явь чистой воды."
        moxie "Теперь моя очередь задавать вопросы. Как тебя зовут?"
        unnamedmc "Меня зовут..."
        python:
            playername = renpy.input("Как тебя зовут?")
            playername = playername.strip()

            if not playername:
                playername = "Анон"
        mc "[playername]"
        show moxie silhouetteneutral
        with dissolve
        moxie "Хорошо [playername]..."
        show moxie closesilhouettesad
        with dissolve
        "Она поднимает книгу и показывает мне открытую страницу."
        moxie "Смотри! Тут написано, что ты не должны быть разумным!"
        mc "е могу ничего разглядеть, тут слишком темно."
        scene bg black with dissolve
        hide moxie closesilhouettesad with dissolve
        "Мокси оборачивается и кладет книгу обратно на стол. Ее рог на мгновение вспыхивает пурпурным светом, и лампа в углу комнаты включается сама."
        play music wagon fadein 6.0
        scene bg moxiewagonlamp
        show moxie shy
        with moxiespell
        "В комнате светлеет, и я могу разглядеть все предельно четко, но все равно не могу поверить в то, что вижу."
        show moxie fullres with dissolve:
          xpos 700
          ypos 700
          linear 10.0 xpos 700 ypos 2750
        "В свете лампы я вижу вызывающе обнаженное создание, ее грудь и многое другое, я вижу даже хвост и рог."
        "Как мне вообще понять, в какую невозможную ситуацию я попал?"
        "Неужели девушка передо мной - единорог? Я совершенно сбит с толку."
        hide moxie fullres with dissolve
        show moxie serious with dissolve
        menu:
            "Что ты подразумеваешь под \"не должен быть разумным\"?":
                show moxie shocked with dissolve
                moxie "Ну, ты создан заклинанием, которое я наложила. Я вызвала временного фамильяра, чтобы тот выполнил мою просьбу."
                moxie "В книге заклинаний написано: \"не разговаривает, не чувствует, просто выполняет приказы\"!"
                moxie "Ты должен был быть безмозглым жеребцом, который делает все, что я захочу."
            "Почему ты называешь меня рабом?":
                show moxie bashful with dissolve
                moxie "Извини! Ты не мой раб, просто во мне говорит высокомерие, мы можем быть на равных, если хочешь!"
                moxie "Я-я просто пыталась сотворить заклинание «Призыв фамильяра», которое вызывает временного фамильяра, исполняющего мои приказы."
                moxie "В книге заклинаний написано: «не разговаривает, не разумен, просто следует приказам».!"
                moxie "Ты должен быть бездумным жеребцом, который делает все, что я захочу."
        show moxie sad with dissolve
        moxie "Ты даже не жеребец ... Блин, насколько же ужасна в магии?"
        mc "Позволь кое-что прояснить, ты наложила заклинание и призвала меня? Это делает меня твоим рабом или фамильяром?"
        show moxie shy with dissolve
        moxie "Ага, это было заклинание «Призыв фамильяра» из книги, которую я взяла в библиотеке у Пенелопы."
        menu:
            "Не верю.":
                show moxie shocked with dissolve
                moxie "Ха?"
                mc "Я не твой фамильяр"
                show moxie shy with dissolve
                mc "У меня есть воспоминания о жизнь, соответственно я не могу быть им."
            "Да, наверное, я результат твоего заклинания.":
                show moxie happy with dissolve
                moxie "О, ты правда так думаешь? Я наложила правильное заклинание и только что сделал «супер-фамильяра»? Может, Пенелопа что-то перепутала..."
                mc "Да уж, возможно, но есть небольшая проблема."
                show moxie serious with dissolve
                moxie "Что такое?"
                mc "Я не могу быть твоим рабом, у меня есть своя жизнь дома."
        mc "Последнее, что я помню,это как я дремал в постели, так что твое заклинание, должно быть, переместло меня оттуда сюда."
        show moxie shocked with dissolve
        moxie "Вау ... У тебя есть воспоминания и все такое?"
        mc "Конечно, я все-таки настоящий человек."
        show moxie serious with dissolve
        moxie "Хм ... Расскажи мне побольше о себе."
        show moxie neutral with dissolve
        mc "ЭЭ, ну, я человек с планеты Земля."
        show moxie shocked with dissolve
        moxie "Так называется наша планета! Но я никогда раньше не слышал о «человеке» ..."
        show moxie laughing with dissolve
        moxie "Я могу только сделать вывод, что великая и могущественная Мокси создала совершенно новую, разумную форму жизни. Это отлично..."
        mc "Я не новая форма! Я настоящий человек!"
        mc "Хотя, и ты, и все остальное для меня новое."
        show moxie shocked with dissolve
        moxie "Шучу, шучу! Да уж, похоже, я совершила волшебное преступление."
        mc "Всего несколько часов назад я играл на компьютере у себя дома."
        show moxie shy with dissolve
        moxie "О да? Расскажи побольше."
        mc "Я учусь в колледже, мне восемнадцать лет."
        menu:
            "Не хочу быть рабом какой-то волшебной пони":
                show moxie bashful with dissolve
                moxie "Эх... Планы изменились, я не хочу настоящего раба."
                moxie "Это была всего лишь маленькая мечта о власти, которую я бы имела над фамильяром, а не каким-то реальным \"человеческим\" чуваком."
            "Я устал, ты можешь отправить меня домой?":
                show moxie sad with dissolve
                moxie "Хм, а я могу? Я не знаю, как обратить это заклинание."
            "Почему я здесь?":
                show moxie embarrassed with dissolve
                moxie "Я тебе уже говорила, я пыталась призвать фамильяра, но, кажется, перепутала заклинание и вместо этого призвала тебя."
            "Почему ты голая?":
                show moxie shy with dissolve
                moxie "Ты ведь тоже голый."
                mc "Ах да, сегодня я спал голышом, потому что было ужасно жарко."
            "Ох, я бы тебя...":
                show moxie horny with dissolve
                moxie "Ох, хе-хе, грязные мыслишки... Держу пари,  фамильяр так не может."
        mc "Вообще, что такое фамильяр?"
        show moxie shy with dissolve
        moxie  "Нуу этоо... эфирное тело, которое может взаимодействовать со планом смертных..."
        "Она говорит, повторяя слово в слово книгу заклинаний"
        show moxie bashful with dissolve
        moxie "Он может выполнять приказы и прочее."
        mc "И зачем ты пыталась призвать это?"
        show moxie serious with dissolve
        moxie "Подойди сюда, давай сядем и поговорим."
        hide moxie serious with dissolve
        "Она выпячивает грудь, садится на диван и похлопывает по подушкам, словно приглашая меня сесть рядом."
        "Когда она отходит на некоторое расстояние, я пользуюсь случаем, чтобы взглянуть и оценить ее нечеловеческое тело."
        show moxie boobs with dissolve
        "Не смотря на то, что мех покрывает почти все тело, я все еще вижу ее соски."
        "Её оголенная грудь великолепна, и я не часто могу увидеть такую красавицу лично."
        show moxie pussy with dissolve
        "Быстро кинув непристойный взгляд между ее ног, я увидел и ее вульву."
        "Неужели эта девка не стесняется своей наготы?"
        show moxie closehorny with dissolve
        "Поймав ее взгляд, я сажусь рядом. Я не совсем понимаю, что происходит, но не могу сосредоточится из-за ее тела."
        "Я чувствую, как ее мягкая шерсть нежно касается моего бедра, это так приятно."
        show moxie closehappy with dissolve
        moxie "Я не могу поверить, что ты появился из-за моего заклинания.... Говорящий... Это круто, но немного страшно!"
        show moxie closelaughing with dissolve
        moxie "Я смотрю, ты не можешь отвести взгляд от моего великолепного тела. А как же твои манеры! Хехе."
        menu:
            "Ну я хочу не только смотреть.":
                show moxie closeembarrassed with dissolve
                moxie "О, правда? Оооо, блин... На самом деле, это как раз то, что я хотела предложить..."
            "Ну извини, так сложно не смотреть на тебя":
                show moxie closehappyneutral with dissolve
                moxie "Хехе, это хорошо [playername]... Мне немножко стыдно, но думаю самое время сказать, зачем я тебя призвала."
            "Сосредоточься, я хочу знать, почему я здесь.":
                show moxie closebashful with dissolve
                moxie "Ну да, ну да... Я как раз собиралась тебе расскзать, а ты пялился на мои сиськи."
        moxie "Видишь ли, великой Мокси нужен кто-нибудь, чтобы поиграть сам знаешь во что."
        show  moxie closehorny with dissolve
        moxie "Ты должен знать, что я могу очень возбудиться."
        "Серьезно? Она призвала меня для секса?"
        "И она говорит мне, что возбуждена?"
        "Она таак близкоо"
        "Этого более чем достаточно, чтобы туда начала приливать кровь."
        menu:
            "Ты призвала меня для секса? Отлично! Когда начнем?":
                show moxie closehorny with dissolve
                moxie "Ахаха, мне нравится твое рвение."
                mc "Ладно, что мы будем делать?"
                show moxie closeshy with dissolve
                moxie "Кх, на самом деле, меня кое-что беспокоит."
            "Я чувствую себя твоей игрушкой и это слегка возбуждает":
                show moxie closeembarrassed with dissolve
                moxie "Игрушкой? Но я же не специально тебя призвала... Так получилось."
                mc "Подожди, значит я могу делать что хочу?"
                mc "Не особо уверен, Мокси."
                show moxie closeshy with dissolve
                moxie "Не, не... [playername]! Наши судьбы связаны, мы сейчас как лучшие друзья."
            "Я твой секс-раб? Даже не знаю, как к этому относиться.":
                show moxie closehorny with dissolve
                moxie "Секс-раб звучит грубовато, как насчет раба, у которого есть секс?"
                mc "Думаю надо еще раз переформулировать выражение, чтобы оно меня удовлетворило."
                show moxie closeshy with dissolve
                moxie "Ну ты понимаешь, что я что-то не то наколдовала, поэтому чувствую себя виноватой в, том, что у тебя ест разум."
                moxie "Я просто хотела безликую безликую секс-игрушку, которая бы меня удовлетворила."
                mc "Это все равно звучит как секс рабсво."
                show moxie closeangry with dissolve
                moxie "Нет, нет, ты не понял. Ты не должен быть разумным.."
                mc "Ох."
        show moxie closebashful with dissolve
        moxie "Я не ожидал, что ты будешь уметь говорить и обладать личностью."
        moxie "Сколько я пыталась быть великой и могучей, у меня никогда не было разумного раба! Это запрещено законом."
        show moxie closeserious with dissolve
        moxie "Я уже смирилась, что ты настоящая личность, а не сексуальная игрушка."
        moxie "А это значит, что ты лишишь девственности великую и могущественную Мокси! Это было бы очень неловко и все такое, я тебя почти не знаю."
        "Она постепенно смирилась с тем, что я реальный человек, равный ей, и это первое, о чем она беспокоится?"
        menu:
            "Забрать твою девственность, разве это не делает все только интересней?":
                show moxie closebashful with dissolve
                moxie  "Отчасти да, отчасти нет."
                show moxie closeshy with dissolve
                moxie "Я думаю, что самая большая проблема заключается в том, что ты мне понравился, и это меня смущает."
                mc "Ууу, как это мило."
            "Эх, не могу поверить, что меня отвергла девушка, которая буквально вызвала меня для секса.":
                show moxie closeshocked with dissolve
                moxie "Что? Я бы ни за что тебя не отвергла. Я просто борюсь внутренним противоречием, из-за того, что мои отношения с {i}настоящим{/i} человеком так быстро развиваются."
                show moxie closehorny with dissolve
                moxie "Вообще-то я всегда хотела чего-то подобного, но это происходит так быстро, что мое сердце колотится как бешенное."
                mc "Я тоже волшебным образом очутился в твоем доме, это и меня слегка ошеломляет."
                moxie "*Вздох*, ты прав, я эгоистка."
        show moxie closebashful with dissolve
        moxie "Это не меняет того,  как я себя чувствую... Я просто сгораю от желания... *Ох*"
        "Сгораю от желания? Если она и дальше продолжит свои грязные разговорчики, у меня точно встанет."
        "Неужели она собирается сидеть здесь и дразнить меня, пока я не сделаю первый шаг?? Или она занята борьбой с противоречивыми чувствами?"
        show moxie closesatisfied with dissolve
        "В этот момент Мокси покорно наклоняется и прижимается к моей груди, я ощущаю тепло ее тела.."
        moxie "Ты даже хорошо пахнешь, вот отстой."
        mc "Ты тоже..."
        "Она как будто специально меня дразнит, я чувствую, что с каждой секундой возбужда.сь все сильнее."
        mc "Я все еще пытаюсь уложить в голове всю эту новую информацию. Ты точно этого хочешь?"
        show moxie closeshy with dissolve
        moxie "Да, наверно...Ты завелся?"
        show moxie closehorny with dissolve
        "Завелся ли я? Этим словом невозможно описать то, что я ощущаю. Я просто пылаю, мой член меня просто не слушается. А она смотрит на него прямо сейчас..."
        "Я чувствую, как в моей груди нарастает стеснение, из-за того, что ситуация затягивается затягиваться. Я не ожидал, что буду так нервничать, но..."
        mc "Это тоже мой первый раз."
        show moxie closesad with dissolve
        moxie "Что ж... Поскольку у нас это впервые, мы должны идти медленно и готовиться к грандиозному финалу."
        mc "Насколько медленно? Как насчет минета?"
        show moxie closeangry with dissolve
        moxie "Ай-ай-ай, чувак, какой же ты лентяй!"
        moxie "Я вызвал тебя сюда, чтобы ты доставил мне удовольствие, а теперь ты просишь меня сделать всю все за тебя?"
        mc "Я тоже тебя вылижу."
        show moxie closehorny with dissolve
        moxie "Наконец-то ты заговорил на моем языке."
        "Мокси наклоняется и приближает свое лицо к моему стояку. Это кажется немного странным, как она и сказала, технически я только что встретил эту девушку, и она даже не человек..."
        mc "Погоди секунду!"
        show moxie closeangry with dissolve
        moxie "Ыы, ты умеешь убить весь настрой."
        show moxie closeneutral with dissolve
        moxie "Понимаю, если ты не хочешь этого делать, я не буду тебя заставлять..."
        mc "Я действительно хочу, но..... Когда я смогу вернуться домой?"
        show moxie closeshocked with dissolve
        moxie "Эм... Вернуться домой?"
        mc "Да, я не могу оставаться здесь вечно; я буду спать с тобой, но потом тебе придется отправить меня обратно."
        moxie "Но... Я понятия не имею, как отправить тебя обратно... Это может занять несколько дней, а может и недель..."
        show moxie closesad with dissolve
        mc "Ох..."
        moxie "Но, клянусь, я сделаю все, что в моих силах, чтобы помочь тебе вернуться.."
        show moxie closehappy with dissolve
        moxie "Пути магии неисповидимы, [playername]. Но я найду этот путь, обещаю.."
        mc "Ладно, я не очень разбираюсь в магии, но верю в тебя."
        show moxie closelaughing with dissolve
        moxie "Ахах, прекрасно! Как насчет того, чтобы обновить сделку?"
        mc "По рукам? Я не знал, что мы заключили сделку."
        show moxie closehappy with dissolve
        moxie "Я буду пытаться отправить тебя обратно, и в обмен на это: Я позволю тебе остаться в моем фургоне, я буду готовить тебе еду и позволю спать в моей супер удобной кровати."
        show moxie closehappyneutral with dissolve
        mc "Oohhh, not bad... And the catch?"
        show moxie closehorny with dissolve
        moxie "Если ты собираешься остаться, тебе нужно будет удовлетворить мои сексуальные желания."
        menu:
            "Сделка заключена.":
                show moxie closehappy with dissolve
                moxie "Шикарно! Давай не будем ждать, а начнем немедленно исполнять твою часть сделки."
                mc "Звучит слишком хорошо, чтобы быть правдой."
            "Ну не знаю...":
                show moxie closesad with dissolve
                moxie "Да уж... опять я все испортила, теперь тебе некуда идти."
                mc "Ну... Возможно ты права..."
                "Мне надо взвесить все \"за\" и \"против\"... Если я действительно застрял в другом мире, мне, вероятно, потребуются все друзья и связи, которые я могу получить."
                mc "Ладно, придется согласится; а пока я получаю свой минет."
                show moxie closehappy with dissolve
                moxie "Шикарно! Давай не будем ждать, а начнем немедленно исполнять твою часть сделки."
    label intro53:
        $ intro69replay = 0
    label intro69:
        stop music fadeout 5.0
        show moxie closehorny with dissolve
        "Медленно спускаясь от груди к моим бедрам, Мокси оказывается у меня между ног. Она замерла, зачаровано смотря на мой член, будто обдумывая свои дальнейшие действия."
        moxie "Ого, какой большой, не правда? Я точно не знаю, мне так кажется. Я просто так вижу… Ох, я словно таю..."
        "Она выглядит наивной, и это даже мило; она охватило древко одной рукой и начала неумело совершать возвратно-поступательные движения вверх и вниз."
        "Это явно ее первый раз, так как она экспериментирует и примеряется к моему член."
        moxie "При взгляде на него мне становится так жарко, я никогда раньше так не пылала."
        hide moxie closehorny with dissolve
        play music sex1 fadein 40.0
        play ambience blowjob
        show moxieb blowjob
        show moxie blowjob2
        with dissolve
        "Мокси подвинулась поближе и тихонько придвинула свою мордочку к вершине моего древка, все это время она просто не сводила с него глаз. Она робко открывает рот и засовывает его кончик внутрь."
        show moxie blowjob1 with dissolve
        moxie "Ааах, э-это технически мой первый раз в жизни… Но это ведь не считается, да? Ты просто моя игрушка.…"
        mc "Погоди, ты же сказал, что я не секс - игрушка."
        moxie "Ехехе, подыгрывать мне, [playername], от этого становится еще жарче..."
        show moxie blowjob2 with dissolve
        "Она высунула свой язычок и нежно прижала его к моему члену, двигая его взад и вперед. "
        "Ее язык горячий и влажный, гораздо длинее, чем у человека.. Я чувствую это тепло от основания моего ствола до кончику, оно окутавет всю его длину, небрежно погружая его в слюну. "
        show moxie blowjob1 with dissolve
        moxie "*Ммммфхх* Я просто не соображаю… Нет, нет, я совсем не могу думать.…"
        "Ее бессвязное бормотание звучит очень мило. Пока ее язычок работает с кончиком, рука занята основанием, двигаясь вверх и вниз "
        show moxie blowjob3 with dissolve
        moxie "*Ммфхх* *Чмок* *Лизь* *Глоть*"
        "Изо рта капает слюна, есть что-то первобытное и похотливое в ее движениях. "
        "Хотя она делает неаккуртано, ее язык грубо наматывает круги вокруг самой чувствительной части верхушки. Она даже не успевает вздохнуть.."
        show moxie blowjob1 with dissolve
        moxie "Он дрожит… Прямо как я… *Ммффх* *Лизь*"
        show moxie blowjob2 with dissolve
        "Её свободная рука скользнула вниз, я могу только представить, как горячо она гладит жаждующую киску. А вот чего я не могу себе представить, так это насколько непреодолимое желание охватывает ее, похоже, она уже почти не контролирует себя.. "
        "Я позволяю себе откинуться на диван Мокси, сначала я немного нервничал, но это не так уж плохо. Раньше у меня был только один минет, но этот гораздо лучше, ее длинный, теплый и влажный язык кажутся нереальными. "
        show moxie blowjob3 with dissolve
        "Я кладу руку на голову Мокси, и глажу её, пока она лижет мой член, её волосы невозможно мягкие. Еще у нее есть милые пушистые ушки, которые дрожат, когда я к ним прикасаюсь, все это выглядит нереалистично."
        "Мокси опускается и берет мой член в свой горячий рот. Обернувшись губами вокруг моего древка, она «трахает» меня своим ртом, пока ее язык творит свою магию.."
        moxie "*Мммффх* *Хлюп* *Хлююп*"
        "Я чувствую каждое движение ее языка, когда он кружит по моему стволу; это кажется нереальным. Если бы я не передернул перед сном, я был бы близок к тому, чтобы кончить прямо сейчас."
        stop ambience
        "Мокси отрывается от моего члена, тяжело дыша, там внизу так мокро, будто весь мой член теперь смазан ее слюной. Похоже, она так увлеклась, забыла дышать."
        moxie "П-пожалуйста, засунуть в меня пальцы, пока я давлюсь твоим членом? Я хочу представить, как меня трахают."
        "Несмотря на пьянящее ощущение эйфории от минета, я осознал, что бедная Мокси с каждой секундой возбуждается и жаждет все сильнее"
        play ambience blowjob
        show moxieb sixtynine
        show moxie sixtynine1
        with dissolve
        "Она поворачивается на бок и знаком приказывает мне лечь.. Я следую ее приказу и она снова занимает свое место, теперь она лежит на мне своим животом. Мы очутились в позиции №69, и ее сочная киска находится настолько близко, что мое лицо ощущает жар, исходящий от нее."
        "Это первый раз, когда я лично вижу что-то подобное так близко. Однако Мокси - не обычная девушка. Ее выпяченная вульва, окаймленная шерсткой, влечет меня."
        "Ее киска блестит от влаги, ни одна человеческая девка с ней в этом не сравнится, шерстка вокруг ее вульвы пропитана ее похотью."
        show moxie sixtynine2 with dissolve
        "Я вытягиваю язык и начинаю робко исследовать ее пещерку. Это определенно наш новый опыт и Мокси вздрагивает от каждого движения языка."
        moxie "Ах-ах! О дааа… *Лизь*"
        show moxie sixtynine3 with dissolve
        "Мокси вернулась к моему члену, снова взяв его в рот, в то время как мой язык начал скользить вверх и вниз по ее похотливой киске. Она определенно наслаждается этим, я слышу как она мило стонет при каждом движении моего языка. "
        show moxie sixtynine2 with dissolve
        moxie "Мммфх… Полижи клитор тоже, пожалуйста! *Хлмпфх*"
        show moxie sixtynine3 with dissolve
        "Хоть это и первый раз, когда я лижу тяночке, но я точно знаю, где находится клитор, я вижу, как он набух и выглядывает из-под капюшона."
        "Я тяну ее круп к своему лицу и начинаю лизать клитор вверх и вниз. Мокси отвечает с энтузиазмом, двигая бедрами взад и вперед по моему лицу. "
        "Когда я дотронулся до ее клитора языком, она задрожала от удовольствия, и минет стал еще более первобытным и грязным."
        "Однако, пока я ублажал Мокси, она не сдерживалась. Она целенаправлено ласкала мою головку своим мокрым язычком, одновременно помогая рукой."
        "Это чистая фантастика, как будто я дрочу и одновременно кто-то сосет, эти точные движения наполняли меня неизмеримым удовольствием."
        show moxie sixtynine2 with dissolve
        moxie "Ахх… Ах… Твой член пульсирует… Ммфхх *Лизь* Скоро кончишь? "
        show moxie sixtynine3 with dissolve
        "Она продолжала повторять одни и те же движения, ускоряясь по мере роста ее желания. Это ошеломляюще, такого никогда не было, и я чувствовал, как близится кульминация. "
        "Становилось все труднее сосредоточиться на лизании, но Мокси, казалось, была в эйфории, несмотря на мою любительскую работу языком."
        show moxie sixtynine2 with dissolve
        moxie "Охх… Как же хорошо, продолжай, [playername], ахх!"
        show moxie sixtynine3 with dissolve
        "По мере того как удовольствие поглощало меня, я стралася лизать ее клитор так быстро, как мог, мой язык даже начал побаливать, но ее стоны и то, как она извивалось на моей груди, подстегивали меня."

        "Мне кажется, ей осталось немного; я тоже уже на грани. Мой член пульсировал и напрягался сильнее, чем когда-либо прежде, я уверен, что сейчас получу самый мощный оргазм в своей жизни."

        moxie "Б-ьлизко… Ааахх! *Шлрп* *лизь*."

        "Меня всего трясло от переполняющих ощущений и страсти.. Я чувствую, как мой оргазм стремительно приближается."

        moxie "Мммффх… Кончаю, я кончаюю!!"
        stop sound
        play sound cum
        show moxie sixtynine4 with cum
        "Её сладостные стоны и восхитительный ротик с лёгкостью довели меня до высшей точки наслаждения, наконец-то сдавшись, я взорвался, и струя горячего семени ударила ей прямо в нёбо"
        play sound cum
        show moxie sixtynine4 with cum
        play sound cum
        show moxie sixtynine4 with cum
        moxie "Ах, аахх… Дааа *Глоть* *Лизь*"
        play sound cum
        show moxie sixtynine4 with cum
        play sound cum
        show moxie sixtynine4 with cum
        "Мокси проглатывает безо всяких колебаний проглатывает все, что вытекает из моей головки, слизывая все остатки, я и не думал, что могу так обильно кончить."
        play sound cum
        show moxie sixtynine4 with cum
        play sound cum
        show moxie sixtynine4 with cum
        "Я продолжал кончать, все больше спермы выплескивалось в рот Мокси, это было похоже на абсолютное блаженство."
        "Когда мой оргазм рассеялся, я почувствовал комфорт и расслабление во всем теле. Это был потрясающе мощный оргазм, так что я чувствовал себя немного усталым."
        show moxie sixtynine5 with dissolve
        moxie "Мммфх… Т-так много… *Глоть* Так горячо…"
        scene bg black with dissolve
        stop music fadeout 2.0
        stop ambience fadeout 2.0
        "..."
        if crystalballactivated == 1:
            $ crystalballactivated = 0
            jump cbmenu
        show bg moxiewagonlamp with dissolve
        show moxie closehappyneutral with dissolve
        play music wagon fadein 150.0
        "Почистившись от остатков спермы, Мокси ловко развернулась и улеглась на моей груди."
        moxie "*Фуух* Это было слишком хорошо, я трижды дошла до финиша… *Pant*"
        "Три раза? Ух ты, а мне показалось, что всего лишь раз."
        show moxie closelaughing with dissolve
    moxie "Ты тоже много кончил! Ха, ну естественно; это было не удивительно с моей-то продвинутой техникой! … *Фух*"
        mc "Это просто невероятно, твой язык вытвторял что-то такое, что я никогда не испытывал раньше."
        moxie  "Ты тоже сделал все идеально, ты это все, что я хочу, и даже больше.."
        show moxie closesatisfied with dissolve
        mc "А ведь это было всего лишь рот?"
        moxie "Не беспокойся, это маленькое столкновение утолит мой аппетит лишь на время, но в следующий раз мне понадобится больше."
        mc "Как это великодушно с твоей стороны. У меня есть еще вопросы, но я не могу думать ни о чем, кроме как упасть в постель и заснуть прямо сейчас.."
        show moxie closealthappy with dissolve
        moxie "Тогда тебе понравится моя кровать, она очень удобная."
        mc "Ладно, я готов хорошенько вздремнуть."
        show moxie althappy with dissolve
        "Вместе мы встаем с дивана и она ведет меня в отдельную комнату своего изящного фургона."
        "Ее фургончик выглядит компактно, при это он не так уж и мал. Здесь достаточно места для спальни, ванной, кухни и гостиной."
        hide moxie happy with dissolve
        show bg moxiebednight with dissolve
        "Her bedroom is essentially only a closet and a double bed; the floor space is almost non-existent except for the doorway."
        "I don't care about that right now though, this bed looks incredibly cosy."
        "Moxie jumps on the bed and crawls up to the pillows on all fours, I slink my way to her side and bury myself under the comfortable covers. "
        show moxie closesatisfied with dissolve
        "She slips under the covers with me and snuggles quite close to me. It seems she’s tired too; I’m not surprised. What a night."
        moxie "Goodnight [playername]."
        "I wonder if everything will go back to normal when I wake up."
        mc "Goodnight Moxie."
        hide moxie closesatisfied with dissolve
        show bg black with dissolve
        stop music fadeout 8.0
        "I can feel the soft fur of her thighs tangle against the bare skin of mine."
        "It feels luxurious, like I could just melt away in this bed."
        "It’s so… "
        "It’s…"
        "Comfy…"
        "…"
        "……"
        "………"
        if crystalballdayactivated == 1:
            $ crystalballdayactivated = 0
            jump cbmenu
        jump prologueday2
    label prologueday2:
        play ambience ambienceday
        mc "Mmphh…"
        scene bg moxiebedday with dissolve
        "My eyes open, the blinds aren’t black-out so I can tell its day outside…"
        show moxie closehorny with dissolve
        "Yep, Moxie is there, still. In fact, she’s looking directly at me. Her expression feels so delicate, her lips are slightly parted and there’s a dreamy look in her eyes. "
        show moxie closesatisfied with dissolve
        show moxie closehorny with dissolve
        "She looks down for a moment her expression unchanging. She was caught staring at me, but she doesn’t seem embarrassed. "
        mc "I’m still here."
        show moxie closesatisfied with dissolve
        moxie "You’re still here… I’m glad."
        mc "Really? I thought I might be a nuisance for you. "
        show moxie closealthappy with dissolve
        moxie "Shh… You aren’t… You've got your uses, hehe..."
        moxie "It’s pretty late in the morning. I’m usually awake by now, but I don’t really feel like getting out of bed."
        show moxie closesatisfied with dissolve
        "She gets even closer; I can feel her warmth and her softness. Her chest presses against mine."
        moxie "You can cuddle me if you want."
        "Taking the invitation, I wrap one of my arms around her, it feels good."
        show moxie closealthappy with dissolve
        moxie "But if anyone asks, we never did anything sexual, or cute! I know I’ve been quite open and honest with you, but I have a cool persona I need to keep up when we go to meet my friends."
        mc "Aren’t you going to keep me locked in your wagon like some kind of secret?"
        show moxie closelaughing with dissolve
        moxie "Not a chance, I need to show you off and brag about how accomplished I’ve become as a spell caster. You’re my magnum opus."
        hide moxie closelaughing with dissolve
        "She shifts onto her back and gazes at the roof, my eyes follow hers and I notice an adorable star constellation poster above us."
        scene bg moxiebedroof with dissolve
        moxie "My best friend is kind of a magic nerd and she has some crazy connections, she'll definitely have some good plans for you."
        moxie "We'll go and see her, but... Let's snuggle first."
        moxie "I actually wouldn’t be surprised if they just figured out a way to send you back immediately. "
        mc "That would be a little anticlimactic, I wouldn’t even get the opportunity to properly uphold the deal."
        moxie "Yeah… Totally not fair, I go through all of that work only for you to disappear. "
        moxie "Which is why you should spend one more night with me, even if we figure out how to send you back. Promise?"
        "I briefly have a flashback to my home life... It’ll take a few days before people notice I’ve gone missing, I don’t want to worry anyone, but these are unusual times."
        "I’ll have to accept the circumstances and push on. Moxie is my beacon of hope, it's the least I could do."
        menu:
            "I promise.":
                moxie "Hehe, thank you."
            "I should get back as soon as I can.":
                moxie "That's okay too..."
        scene bg black with dissolve
        "..."
        play ambience ambienceday
        scene bg worldmapdialogue with dissolve
        "We snuggled for about thirty minutes before leaving. The thing that scared me most about this wasn’t just meeting new strange people of a different species, but it was the cultural differences."
        "Ponies don’t wear clothes, she told me, and that meant neither should I."
        "I have to walk around naked with my flaccid penis limp between my legs. I'll never get used to this."
        scene bg arcadiasuburbs with dissolve
        show moxie happyneutral with dissolve
        "This is unbearably embarrassing, but Moxie assured me it was completely normal. She certainly didn’t seem to mind bearing all, so I just uncomfortably followed suit."
        "The worst part is that everyone we passed on our way to the library glanced at me, some briefly, some staring."
        "I’d probably stare if there was a naked pony girl walking down my street too, but that thought didn’t make me feel any better about the situation."
        "All the bystanders were female too, I didn’t see any males, so I didn’t even have the comfort of relating to any other nude males."
        "That being said, the ladies were also nude, that helped take off some of the embarrassment. Fairly sure I’ve seen more boobs today already than I have throughout my entire life."
        hide moxie happyneutral with dissolve
        show bg tree1 with dissolve
        "The two of us arrive to a towering tree, taller than all the surrounding buildings."
        mc "What's up with this big tree?"
        show bg tree2 with dissolve
        show moxie laughing with dissolve
        moxie "This is Lily's library."
        mc "Woah, there's a library in here?"
        moxie "My best friend Penelope works here, just let me do the talking and answer questions if you’re asked, okay?"
        show moxie closehappy with dissolve
        "Moxie pats me on the shoulder and whispers into my ear reassuringly."
        moxie "I know this may be awkward for you, but I’ll try to make this as painless as possible."
        hide moxie closehappy with dissolve
        scene bg library with dissolve
        stop ambience fadeout 1.0
        "With that, she opened the door and stepped into the library. I don’t often step foot into libraries, but there was something truly magical about this one."
        "Not only was the entire interior finely decorated but there were books as far as the eye could see."
        play music suspense fadein 40.0
        "As my eyes scanned across the room, I soon spotted another individual, only one though, I guess libraries aren’t popular even in this world."
        "Moxie cracked her fingers in a smooth motion before walking towards the blue mare that was tinkering with some books deeper into the library, I kept pace behind her."
        show moxie happyneutral with dissolve:
            xpos 700
            ypos -30
        moxie "Penny!! I have great news and I have bad news, but mostly great news!"
        show penelope neutral with dissolve:
            xpos 200
            ypos 30
        show moxie shy with dissolve:
        penelope "Heyy Mox, you brought a... familiar...? What the heck is that thing... I can already see that this one is mostly bad news, right?"
        "'Penelope' raised an eyebrow while making eye contact with me. She stared me down in disbelief, I too stared her down in equal disbelief..."
        "This is the second pony I've seen up close... Blue fur, just like Moxie, but she seems to have a slightly different nipple pigment, and her purple hair and green eyes are really striking!"
        "I walked past many strange denizens on the way here too, it's all so alien to me."
        show penelope laughing with dissolve
        penelope "I have never seen something like that before in my entire life, did you accidentally defluff a stallion?"
        show moxie laughing with dissolve
        moxie "Oh, he’s not so bad, he’s my familiar! From that spell you told me about, remember? I totally nailed it, I blew that spell’s expectations out of the water, he can talk!"
        show penelope shy with dissolve
        penelope "Come on Moxie, you know that’s not how it works, that spell had limitations. We just wanted a temporary familiar, right?"
        show moxie shy with dissolve
        penelope "I don’t know what you ended up casting but I’m pretty sure familiars aren’t supposed to look like that. Between you and me, mine had boobs."
        "I instinctively check my chest. I haven't seen myself in a mirror since I arrived, fortunately everything seems to be as usual."
        show penelope shocked with dissolve
        penelope "This is… some kind of hairless pony… I suppose he’s pleasant to look at, but… it’s just bizarre. I doubt we can do anything with this."
        show penelope neutral with dissolve
        penelope "Unless this is a strange familiar, it looks to me like you cast the wrong spell, Moxie."
        show moxie sad with dissolve
        moxie "Ahaha, ha… yeah, maybe... Look though, this is so much better than a familiar, I was serious when I said he can talk!"
        penelope "Talk? You said that earlier, but he hasn't said anything..."
        moxie "Oh, right! I told him to leave the talking to me, sorry!"
        "Moxie gently nudges me as if trying to get me to perform. I realize I’ve been so caught up in thought that I haven’t said anything yet."
        "I'm still not used to this, meeting people, being naked, being different."
        show moxie neutral with dissolve
        menu:
            "Uh, hi":
                show penelope embarrassed with dissolve
                penelope "Oh... It talks, hello."
            "Nice to meet you, I'm [playername].":
                show penelope embarrassed with dissolve
                penelope "... Nice to meet you too? I'm Penelope."
            "I don't know what's going on.":
                show penelope embarrassed with dissolve
                penelope "Huh, you can talk..."
        "Penelope was truly shocked when she heard me speak."
        penelope "You… tried to summon a familiar and this person appeared? Moxie, Moxie… I thought this might have been a trick, but… if I were to believe you, this is incredible!"
        show moxie laughing with dissolve
        moxie "Ehehe, well… here’s everything I know so far."
        hide moxie with None
        hide penelope with dissolve
        scene bg black with dissolve
        stop music fadeout 5.0
        "…"
        play music library fadein 5.0
        scene bg library with dissolve
        show moxie bashful with dissolve:
            xpos 700
            ypos -30
        show penelope happy with dissolve:
            xpos 200
            ypos 30
        "A short discussion was had between the three of us. I properly introduced myself and Moxie explained the events of the evening prior with the sexual details omitted. "
        show penelope laughing with dissolve
        penelope "Why, yes, I have heard of this before, I believe Lily has dabbled in this field of magic."
        moxie "Meh, it would be her."
        show penelope happy with dissolve
        show moxie althappy with dissolve
        penelope "Familiars aren't supposed to be permanent, they're supposed to disappear after a while, but our friend here has stuck around."
        moxie "Mhm, he's been here over twelve hours now."
        penelope "With that being said, my hypothesis is that you didn’t 'Create' [playername], you 'Summoned' [playername] from a far off place."
        penelope "I know that might seem confusing, but I don’t think you cast the right spell. Or, the spell had a drastically unintended effect."
        "Although both Moxie and I had already assumed that was the case, it doesn’t hurt to have a third opinion from an expert."
        show moxie shy with dissolve
        show penelope shy with dissolve
        penelope "I think we should forget everything we know about the familiar spell; this is a different spell entirely. I don’t even think it’s in the same category of magic, it could be cosmic magic..."
        moxie "What makes you say that? Whether creating a familiar or a summoning a [playername], the end result totally has the same effect."
        show penelope neutral with dissolve
        penelope "Complicated creation spells always have a time limit, always, it’s simply a law of magic, you can’t conjure a being longer than your magical powers permit."
        penelope "If the spell had a time limit of say… a month instead of thirty minutes, it would be immensely more difficult to cast because it’d need exponentially more magical power."
        mc "Makes sense to me."
        show moxie neutral with dissolve
        "Moxie waves her hand as if to say it doesn’t really matter."
        mc "So I'm stuck here?"
        show penelope shy with dissolve
        show moxie sad with dissolve
        penelope "Perhaps... Allow me to summarise: [playername] doesn’t have a time limit, his existence here is not on the whims of your magical power."
        "This line perks Moxie’s attention, I don’t know the details of magic, but I guess deep down inside she must have still been worried that I’d vanish."
        "Penelope gets a little quiet, seemingly deep in thought."
        penelope "Did you bring back that spell tome? I think there’s something in there that could help explain this conundrum."
        show moxie shocked with dissolve
        moxie "Back? Ah... Woops, did you want it back? I was keeping it just in case."
        penelope "Well, I did ask for it back today, and it looks like you don’t need that spell anymore."
        show moxie bashful with dissolve
        moxie "Uu… Meanie…"
        penelope "There's no rush. Bring it back whenever you get the chance, there’s something I need to check regarding this situation."
        show moxie shy with dissolve
        show penelope laughing with dissolve
        penelope "You know what, I think I’ve got it! I was reading about this and cosmic magic only a month ago."
        penelope "The spell you casted, it must have been… must have been… teleportation."
        penelope "So... Moxie can do that... Teleportation, interesting... There are a few other feasible answers, but I like to stick with the most probable."
        show penelope neutral with dissolve
        "There are a few seconds of silence. Moxie seems unsure while Penelope’s excitement soon dies down as if she realized how unphased we are by her amazing revelation, and the disappointment of that realisation set in."
        show moxie serious with dissolve
        moxie "Just teleportation…? I don't get it, I definitely don't know how to do that."
        penelope "That’s the only spell that comes to mind that is able to circumvent a time limit. Teleportation has permanence to it."
        penelope "I can create a banana out of nothing, and maybe it lasts thirty minutes. But if I teleport a banana, it remains forever."
        show moxie happy with dissolve
        moxie "Well... If that's true, that's great news. We can easily teleport him back!"
        show penelope sad with dissolve
        stop music fadeout 4.0
        penelope "I’m afraid not Moxie, sending him back may be impossible."
        show moxie sad with dissolve
        mc "Impossible?!"
        show moxie angry with dissolve
        moxie "That doesn’t make any sense! If I could bring him here with magic, that means we can use magic to send him back when we're done."
        "Penelope slowly shakes her head, placing her hand on Moxie’s shoulder, she speaks directly to her."
        show penelope shy with dissolve
        show moxie sad with dissolve
        penelope "I know you have a great passion for magic Moxie, but there's still a lot you may not understand..."
        penelope "The problem with teleportation is that it comes with some serious adverse side effects."
        show moxie shy with dissolve
        moxie "Huh? Side effects?"
        penelope "I think Moxie and I need to have a quick private conversation."
        penelope "[playername], could you take a seat at the sitting area while you wait? I'll bring us some tea when we're done and fill you in."
        scene bg black with dissolve
        "…"
        play music uhoh fadein 5.0
        scene bg library2 with dissolve
        "I sat on a chair at a quaint sitting area by the library’s reception. Moxie and Penelope were talking in private while I waited."
        "Moxie returned first with our tea, it was purple, and the flavour was outlandish yet curiously enjoyable."
        show moxie closealthappy at right with dissolve
        "Moxie was shortly followed by Penelope sitting opposite to us across the table."
        show penelope closehappy at left with dissolve
        penelope "I hope the tea is to your liking, [playername]. I’m afraid what I’m about to say may not be."
        show penelope closeneutral with dissolve
        show moxie closeneutral with dissolve
        penelope "Now this isn’t my area of expertise, just a few ideas I’ve learnt from working closely with Lily, so this may not be completely accurate."
        "I want to ask who Lily is, I’ve heard that name thrown around a few times, but I dare not interrupt."
        penelope "The act of teleportation typically involves the recreation of your atomic composition."
        penelope "If your memories of a previous world are true, that means there is, or was, an original version of you."
        penelope "This individual must have either been copied and pasted, or morbidly, cut and pasted."
        mc "Why though? Why can’t it be the same me?"
        show penelope closeshy with dissolve
        penelope "It’s impossible to transport a living being faster than the speed of light, true teleportation is to re-create your body atom by atom."
        show moxie closeserious with dissolve
        moxie "So even if we did send him back, we’d either still have him here, or we’d essentially be killing the original, only to replace him with a teleported copy… "
        "The original me may already be dead, I can only hope I was copied instead of cut like Penelope explained."
        mc "That's like a philosophical zombie."
        mc "If this is all true, that means I'm just a replica of my original self."
        mc "And even if you were to send me back, you'd just create another replica."
        show penelope closeshocked with dissolve
        penelope "Exactly, wow, you're even quicker than Moxie."
        moxie "Pfft, don't gang up on me, I'm totally keeping up."
        show moxie closesad with dissolve
        mc "If this is all true, I don’t even know if I want to try going back. This mind, me, my consciousness, would cease to exist, only to be replaced by a replica that shares all my memories."
        penelope "If I were you, I'd forget your past life, and get used to living here."
        penelope "There's a high probability that the original version of you is doing just fine, so don't worry."
        $ goback = 0
    label librarynewlife:
        menu:
            "Okay, I'll live a new life here.":
                show moxie closehappy with dissolve
                show penelope closehappy with dissolve
                moxie "That's good news, I think!"
                penelope "I know it's a lot to take in, so I'll lend you the utmost support."
                mc "Thank you, there's no point in being negative. It's just like moving to a new city, right?"
                show moxie closelaughing with dissolve
                moxie "Ohh yeah, I did that recently too, we're in the same boat!"
                mc "Let's live the best lives we can then Mox."
                "Moxie and I high-five."
                show penelope closelaughing with dissolve
                penelope "Awhahah, this is sweet to see."
                moxie "I reckon you and me have a lot to discuss regarding living arrangements then."
                penelope "You certainly do, feel free to come here for advice, either of you."
            "I want to go back.":
                if goback == 3:
                    penelope "You're still... Are you really so against living here?"
                    show moxie closetears with dissolve
                    moxie "Come on [playername], I'll do my best..."
                    penelope "You're making Moxie cry."
                    moxie "I-I'm not!"
                    jump librarynewlife
                $ goback += 1
                if goback == 1:
                    show penelope closesad with dissolve
                    show moxie closeshy with dissolve
                    penelope "I'm afraid that might not be possible."
                    penelope "Even if we knew where you're from, the original you may still be alive."
                    mc "That would be complicated..."
                    penelope "What do you think, then?"
                if goback == 2:
                    penelope "You're really adamant about going back..."
                    penelope "I guarantee you this won't work out the way you're hoping."
                    penelope "Even if we do send you back, you'll literally still be here!"
                    penelope "Remember, the philosophical zombie thing you mentioned?"
                    mc "Shit, you're right... It's impossible for this body and brain of mine to go back."
                    penelope "Please reconsider."
                jump librarynewlife
        penelope "Perfect!"
        show moxie closeshy with dissolve
        moxie "Is it time? Should I...?"
        show penelope closehappy with dissolve
        penelope "Yep. Now, since you're a new creature to this world, we need to cast a few essential spells in order to acclimatize your body to the new surroundings."
        mc "Eh? What do you mean?"
        show moxie closehappy with dissolve
        moxie "What Penelope is saying is, you're full of alien bacteria, so you could infect us with something deadly!"
        show penelope closeneutral with dissolve
        penelope "And vice versa, it'd be such a shame for you to die of an illness."
        penelope "Moxie, can you do the honours?"
        show moxie closelaughing with dissolve
        moxie "No problem, don't move an inch, [playername]!"
        play sound magic2
        show moxie closelaughing with moxiespell
        pause 0.5
        play sound magic2
        show moxie closelaughing with moxiespell
        "Moxie cast two spells on me, her horn encapsulating me in a magical glow each time."
        "My balls tingle slightly, as the light dissipates. I've never had magic cast on me before, it's weird."
        show penelope closehappy with dissolve
        penelope "Perfect, I guess he's all set to be let loose on the world?"
        show moxie closehappy with dissolve
        moxie "Hehe, it worked! This is gonna be so much fun!"
        mc "There's one more thing though, could I at least check to see if the original me is alive?"
        show moxie closeneutral with dissolve
        show penelope closeneutral with dissolve
        penelope "I’m afraid we have no way to know where you’re from. Teleportation magic requires the caster to think of mental ‘coordinates’. It’s hard to explain."
        show moxie closeneutral with dissolve
        moxie "I think what Penny is saying is that when I cast the spell before, I misfired, meaning I accidentally used a completely random coordinate that just happened to be on you [playername]."
        show penelope closeshocked with dissolve
        penelope "Random? There’s no way I could accept that. You could misfire that spell ad infinitum and never get the same result."
        penelope "There’s more to this, it’s just a hunch, but there are no coincidences of this magnitude in magic."
        show penelope closehappy with dissolve
        show moxie closealthappy with dissolve
        moxie "This is kinda exciting if you think about it positively, the three of us solving a mystery. The rookie from a galaxy far away, the passionate performer and the genius librarian!"
        show penelope closeshocked with dissolve
        penelope "Hold up, I thought we already solved the mystery."
        moxie "Yeah, but [playername] is my magnum opus, so if I write a paper on him, I need to be as accurate as possible!"
        mc "I'm a scientific study now?"
        moxie "You're a magical study! Once they find out about you, I'll get into college for sure."
        penelope "Eh... I’m a little too busy to get involved with these shenanigans right now. I’m working here almost every day while trying to finish my own papers, specifically in this season too, pain in the ass."
        show moxie closeserious with dissolve
        "Moxie’s enthusiasm deflates, she hunches over as she sinks into the chair."
        show penelope closesatisfied with dissolve
        penelope "Oh Mox, I’ll help you a little, I guess, just don’t expect too much."
        show penelope closelaughing with dissolve
        penelope "You know what? Moxie, you've already done something stupendous, even I'm still trying to rationalise what happened in my head."
        penelope "Moxie, if you can figure this out and present it to the college, there will be no doubt about how amazing and talented you are, you’ll get in for sure."
        show moxie closesatisfied with dissolve
        moxie "Ah Penny, you’re being too kind again, you know this kind of thing is way over my head… But I’ll do my best."
        show moxie closealthappy with dissolve
        penelope "Don’t worry, I’ll try to give you a bit of a head start, I’m pretty curious about how this situation might unfold myself."
        show penelope closehappy with dissolve
        penelope "There are two things I think you'll need to investigate first, the book of course, and the area surrounding where [playername] first appeared, and I want you to figure out their significance if you can."
        show moxie closehappyneutral with dissolve
        penelope "Oh, and next time you visit, bring the book and anything you find, we'll talk through it together"
        show  moxie closehappy with dissolve
        "Seemingly giddy, Moxie jumps up and nods."
        moxie "You’ve got it! Anything out of the ordinary and the book. I’ll see you soon Penny."
        "Moxie turns to me and gestures for us to head out, practically skipping as she does so."
        hide moxie closehappy with dissolve
        penelope "Go get her, tiger."
        "I wink to Penelope, I will."
        hide penelope closehappy with dissolve
        scene bg black with dissolve
        stop music fadeout 5.0
        "…"
        scene bg worldmapdialogue with dissolve
        play music day fadein 5.0
        play ambience ambienceday fadein 5.0
        "I assume we're going back to the wagon, I’m not sure, I'm just following Moxie."
        mc "That was unusual, yet refreshing."
        mc "What do you think, should I just live the best life I can here?"
        show moxie closehappy with dissolve
        moxie "Yes! I'll do everything I can to accommodate you."
        moxie "The people around here are so friendly and accommodating too, I discovered that myself when I moved here."
        mc "Yeah, Penelope was really nice."
        moxie "Penny liked you, y’know! She isn’t usually that friendly and talkative with strangers!"
        mc "She isn’t usually friendly? You could have fooled me, she seems lovely. "
        show moxie closehappyneutral with dissolve
        moxie "That’s just how Penny is, she’s a real softy on the inside, but she has a mature serious side too."
        mc "A softy on the inside, a bit like you then?"
        show moxie closelaughing with dissolve
        moxie "Shush you, lots of girls have a soft side, that’s one of the best parts about them."
        show moxie closealthappy with dissolve
        moxie "Speaking of mature and serious though, Penny scolded me, she made some good points while she and I were talking alone."
        moxie "Thing is, you don’t have a clue about our world, our species, our culture, nothing! It’s not something you can just ignore by hiding in my wagon."
        mc "I’d be open to learn more about those things though, it sounds exciting."
        show bg arcadiasuburbs with dissolve
        show moxie laughing with dissolve
        "Moxie pokes my cheek and runs ahead a few steps before turning back towards me, I stop and look to her earnestly."
        "I wonder if there’s anything serious I need to learn about this world, maybe surprising laws or cultural differences."
        moxie "You’re going to be staying with me in my wagon, that’s the deal we made last night."
        mc "Is the deal still on?"
        show moxie smug with dissolve
        moxie "Ehehe, unless you wanna live on the street, I think so."
        mc "True..."
        show moxie bashful with dissolve
        moxie "Buuut, I was being a little idealistic at the time."
        show moxie althappy with dissolve
        moxie "You can’t just stay at my wagon all day doing nothing, you need to get out there, get a job, meet people, et cetera!"
        show moxie laughing with dissolve
        moxie "I’m gonna release you to the world so you can earn some monies."
        show moxie happy with dissolve
        moxie "Then at night when you come back, I’ll feed you, my treat! I’ve been looking for an excuse to start cooking properly anyway."
        show moxie althappy with dissolve
        moxie "Oh, also! I’ll try to teach you a bit about our culture and society."
        mc "If I'm staying, it makes sense that I learn about this world. Where am I going to work though?"
        show moxie laughing with dissolve
        moxie "Don’t sweat it, we all help each other out in the Arcadian suburbs, it’s a small community. Penny gave me a few suggestions, bless her."
        hide moxie
        show bg worldmapdaynoui
        show wmc1
        with dissolve
        moxie "There’s a farm to the north that specialises in the harvest of apples and various crops, the current owner Honeycrisp seems to have some kind of injury right now and is looking for help."
        hide wmc1
        show wmc2
        with dissolve
        moxie "Next to my wagon just slightly to the east you may have noticed a large round building."
        moxie "That's Ruby’s boutique, she works here making a designer fashion line. I design my own clothes too, so I think it’d be fun to work there, but maybe too difficult for me."
        hide wmc2
        show wmc3
        with dissolve
        moxie "Also, Cream has this delicious cake shop near the market, all homemade and very delicious. Just be careful, she's a little unpredictable!"
        hide wmc3
        show wmc4
        with dissolve
        moxie "Can’t forget Riku, she’s running a quaint bar out of the ground floor of her own house, she’s doing really well for herself and should hopefully take you in on a small wage. Sometimes in the evening me and some of the girls meet up there for a drink."
        hide wmc4
        show wmc5
        with dissolve
        moxie "Well, there’s one girl that seldom drinks, and that would be Butters. She’s some kind of alchemist or something. Ridiculously shy though, there’s probably not much point in going to work with her, but maybe you’re into shy girls."
        hide wmc5
        show bg arcadiasuburbs
        show moxie althappy
        with dissolve
        mc "That’s quite the selection, I’ve actually never worked any jobs like those. Suppose I should try a few out and see what fits me best."
        show moxie happy with dissolve
        moxie "It’s a pretty flexible situation, you could probably work at the library too if you wanted."
        mc "What about you, can’t we work together?"
        show moxie laughing with dissolve
        moxie "Haha, I wish! Maybe if you could grow a horn and learn magic in a day. I’m a street performer that wows people with basic magic, it’s a temporary thing."
        mc "That’s a surprise, I didn’t think you’d be someone that’d enjoy that."
        show moxie bashful with dissolve
        moxie "Ahh… Well, it's a part of what I enjoy. What I really want to do is explore magic and perhaps one day become a researcher, Penelope is helping by lending me books."
        show moxie shy with dissolve
        moxie "I'll need to go to a college, ideally to the Royal Arcadian College, but I’m not talented enough to pass the tests yet."
        show moxie satisfied with dissolve
        "She lets out a dreamy sigh and looks up into the city. The city has a lot of verticality to it. From the ground level of the suburbs the fantasy castles looks dizzyingly tall."
        hide moxie satisfied with None
        scene bg castle with dissolve
        mc "The University is in the city? I didn’t get a good look on the way to the library, but the castles are stunningly beautiful."
        mc "It sounds like hard work, but I’m sure if you do the reading and study, you’ll be able to make it."
        scene bg arcadiasuburbs with None
        show moxie althappy with dissolve
        moxie "Yeah… I'm glad you said that actually, a lot of people can underestimate how much hard work is required, and hard work is what dreams are made of. "
        "The dizzyingly high castles certainly make a difference to the modest wooden structures of the ground level."
        "The suburbs are small in comparison, this area seems to mostly consist of small homes, inns and a few shops dotted around like the boutique, bakery and bar."
        "It’s cute, like a small community where everyone would know each other. The strange hairless man is probably already the talk of the town."
        mc "When we first walked to the library, I was so tense, but now I’m looking forward to spending my time here and learning more about the world."
        show moxie happy with dissolve
        moxie "Oh yeah? How ‘bout we go get some ice cream and I can teach you more? My treat!"
        mc "Ice cream? Sounds like a delicious idea, weren’t we going to work though?"
        show moxie laughing with dissolve
        moxie "Ahh don’t be silly, I can’t just send you over to the girls’ businesses randomly. First Penny is sending out some magic mail explaining the situation. We’ll probably have a reply by tomorrow. "
        mc "In that case, string me along, I love ice cream."
        hide moxie laughing with dissolve
        scene bg black with dissolve
        stop music fadeout 5.0
        "…"
        play music castle fadein 10.0
        scene bg arcadiasuburbs2 with dissolve
        show moxie closehappyneutral with dissolve
        "Moxie orders us both a whipped ice-cream from a small café that’s only an eye-view away from her wagon."
        "There are a couple of tables with seats outside, but Moxie leads me to a secluded seating area that’s a little further from the others."
        "The ice cream is delicious; it tastes slightly different to anything from back home. "
        "The peculiarity of the taste causes me to take my time and savour each lick. It is delightful. A part of me was worried I’d have to eat hay-burgers."
        "But fortunately, it'd seem the diets of these anthropomorphic ponies are no different than my own."
        show moxie closealthappy with dissolve
        moxie "Any questions? I’m sure you have a lot, right?"
        show moxie closehappy with dissolve
        label day2label2:
            pass
        menu:
            "What should I ask Moxie?"
            "How does the country run? Do you vote?":
                show moxie closebashful with dissolve
                moxie "Huh? Okay... That's a boring question, although it's pretty important I guess."
                show moxie closelaughing with dissolve
                moxie "I’ll break it down in the most fun way I can."
                mc "Sure."
                show moxie closealthappy with dissolve
                moxie "We’re in Arcadia right now, it’s both capital and country, Aurora bless Arcadia and all that."
                moxie "Ah, speaking of Aurora. There’s one ruling group called the Royal Sisters, it’s a monarchy, although egalitarianism is an important aspect of their government."
                label day2label2choice1:
                    menu:
                        "Who are the Royal Sisters?":
                            show moxie closealthappy with dissolve
                            moxie "They’re complicated. Queen Aurora has ruled for millennia  and her younger sister Selene is only marginally younger."
                            "Did I hear that right? Did she just say millennia?!"
                            moxie "I adore Selene, she's this super powerful space-time alicorn and I've really gotten into some of her books."
                            menu:
                                "What's an alicorn?":
                                    show moxie closehappy with dissolve
                                    moxie "That'd be a unicorn with wings. But there's a bit more to it than that."
                                    moxie "Crazy buggers, they seem to live for way longer than us normal folk."
                                    jump day2label2choice2
                                "(Say nothing)":
                                    jump day2label2choice2
                            label day2label2choice2:
                                moxie "Allegedly in old religious texts they raise the sun and the moon, but I don’t think anyone actually believes that in the modern era."
                                mc "Why did they ever believe it if it isn't true?"
                                show moxie closealthappy with dissolve
                                moxie "That's a good question. Not one I could answer though, you'd have to ask the long dead scholars of old scriptures."
                                mc "How do the two sisters rule?"
                                show moxie closehappy with dissolve
                                moxie "They’re benevolent rulers, they’re extraordinary actually and often a role model for society."
                                moxie "It's like they're perfect, almost too perfect, like angels- or better, two guardian goddesses to keep us in check."
                                mc "Wow... Guess I'll have to see it to believe it."
                                moxie "Anything else?"
                                jump day2label2choice1
                        "Monarchy with egalitarianism? You mean a consitutional monarchy?":
                            show moxie closeshocked with dissolve
                            moxie "I'm not entirely sure what it classifies as, they're both monarchy and government. However they take opinions of the public sector deeply into consideration."
                            show moxie closeneutral with dissolve
                            mc "With these Royal Sisters having no opposition it sounds like autocratic authority."
                            moxie "Yeah sure, but these two still carry out the will of the people, they're not dictators."
                            mc "Even without any political parties?"
                            moxie "It seems we haven't a need for any political pluralism. These sisters do such a damn good job no one has bothered to rally an opposing party."
                            moxie "I think it'd be interesting to have more opposition, since politics here is a stagnant pond, but everything has been running so smoothly for the past few centuries that people are content with what we've got."
                            mc "So... this is a society that has managed to find a 'perfect' government?"
                            show moxie closehappy with dissolve
                            moxie "Nothing's perfect, however it's pretty close, and I can't remember the last time I saw someone complain."
                            moxie "The two sisters are practically idolised, they seem to run a damn good country..."
                            menu:
                                "Country? So there are other countries?":
                                    show moxie closelaughing with dissolve
                                    moxie "Of course, you're in ponytown right now. Biggest influx of ponies here."
                                    jump day2label2choice3
                            label day2label2choice3:
                                jump day2label2choice1
                        "Enough about that. (Back)":
                            jump day2label2
            "Are there any laws I need to worry about? I don't want to end up in prison.":
                show moxie closealthappy with dissolve
                moxie "That's a good question. I don't know what your world is like, but with any luck it's similar to this one."
                moxie "No stealing, no killing, no horrible acts that cause harm or misfortune."
                mc "I wasn't planning on killing everyone, I was mostly concerned about smaller things I might miss like jaywalking."
                mc "Like, if I was working, do I have to pay tax? Am I going to be jailed for tax evasion?"
                moxie "Don't worry about that, I'll sort out the boring stuff. You can keep the money, that's just between me and you."
                moxie "We don't live in a strict society, as long as you're a good person you don't need to worry about getting in trouble with the law."
                show moxie closelaughing with dissolve
                moxie "If you do get jailed though, I can't bail you out."
                mc "I'll keep that in mind."
                jump day2label2
            "What's the community in the suburbs like? Social, working, et cetera.":
                show moxie closealthappy with dissolve
                moxie "I haven't been here long but the community is great."
                moxie "I'm definitely on the bottom rungs though, it gets better from here."
                moxie "Crime and disorder are barely existent and there’s tons of opportunity for everyone to flourish in the system, even someone like me."
                moxie "Heck, even you, newbie! You can get a job and make a living as long as you pull your weight."
                mc "That sounds fantastic, almost too good to be true. Although, given all the smiling faces, I can believe it."
                show moxie closehappy with dissolve
                moxie "Yeah, everyone is encouraged to contribute to society, as a result communities form that all help each other. Like the suburbs here. "
                moxie "For example, Honeycrisp farms apples and processes them, sells the resulting booze to Riku at her bar, then we all go drink it."
                moxie "A good community is filled with these happy little cycles where the end result is a bunch of ponies with bellies full of food, drink and happiness."
                "Reminds me of how a village would run back in the olden days, everyone in the village would contribute so the village could run independently."
                jump day2label2
            "That's all.":
                jump day2label3
    label day2label3:
        "After Moxie and I run through the basics of this new world, I feel more confident in my being here."
        "But this place seems too good to be true... Why is everything running so smoothly in this world?"
        "Is it really as simple as magic spells and guardian goddesses that look after everyone? Hmm, Earth probably would be a better place if we had that."
        show moxie closeneutral with dissolve
        moxie "This is hard, I feel like I've barely told you anything."
        mc "Don't worry, this has been very insightful, thank you."
        moxie "I guess the best way for you to learn about our world is simply experiencing it."
        hide moxie closeneutral with dissolve
        "A couple of female ponies walk past and take a peek at me."
        show sistertrio with dissolve
        "I take a peek too, I’m still not quite used to seeing naked women, let alone ponies walk around in broad daylight."
        "The stares feel different from this morning."
        "Now that I’m more comfortable in my own skin, I know that they’re not judging or shocked, they’re genuinely curious."
        "The right most one isn't remotely interested though, she must be the tsundere of the bunch. As expected from a redhead with twin tails."
        "Wow, the one with the blue eyes just winked at me."
        "Are they flirting with me?"
        hide sistertrio with dissolve
        show moxie closelaughing with dissolve
        "Moxie giggles, she caught me staring."
        moxie "I think they like you."
        mc "I'm sure they were just staring because I look weird."
        show moxie closehappy with dissolve
        moxie "You’re unusual, I know, but there’s more reasons than novelty for why girls would look at you. "
        mc "What do you mean by that?"
        moxie "You don’t know? Come on, I bet you can figure it out."
        mc "Are they not staring at me because I’m the first human they’ve ever seen?"
        show moxie closealthappy with dissolve
        moxie "Sure, sure, there’s a little bit of that, but there are plenty of species in this world. I’m sure a dragon, griffon, or neko would get a few curious looks too."
        "Dragons, griffons, and neko huh? I guess it only makes sense that this world has other species, but it’s still surprising to hear it."
        "I finish my ice cream while I try to guess what Moxie is implying, but even as I bite into the cone nothing comes to mind."
        mc "I don’t get what you’re saying."
        show moxie closebashful with dissolve
        moxie "Heh, I can’t believe you haven’t figured it out, even after hanging around me."
        moxie "They’re staring at you because you’re male, it’s pony mating season and men are in hot demand right now."
        "I could feel a rush of blood towards my nethers as she said that, but I’m nude and in public, so I resist getting ahead of myself. "
        mc "That’s crazy, you’re telling me that these humanoid pony girls go into heat?"
        show moxie closehorny with dissolve
        "Moxie looks around innocently and nods, in hindsight everything from last night along with her deal makes a lot more sense now."
        moxie "Haven’t you noticed? I thought males are supposed to notice and get aroused when around females in heat."
        mc "I'm supposed to get aroused? Now that you mention it, I did feel something last night. Even though I was tired and had masturbated only a few hours earlier, I was really horny."
        show moxie closesmug with dissolve
        moxie  "Yeah, you really wanted that blowjob, jerk."
        mc "And I've had girlfriends before, being alone with a girl isn't new to me. Yet I could feel something new and powerful."
        mc "It just felt right."
        show moxie closebashful with dissolve
        moxie "Yeah… I can relate. I felt something from you too, your species and mine are perhaps not so different…"
        show moxie closehorny with dissolve
        moxie "One of the reasons I picked a table that was hidden away from the others is because I wanted this conversation to be private, there’s something I need to say."
        moxie "You can take this as a warning, or an opportunity..."
        moxie "You’re going to be quite popular with the mares, girls may come to you and try to talk to you, perhaps asking you to come to their place for ‘coffee’."
        moxie "It's popular among mares to have sex with other species because there’s no risk of pregnancy. You’ll be coveted simply because you’re a male of a different species."
        menu:
            "That's awesome!":
                show moxie closealthappy with dissolve
                mc "What a great role reversal, the girls will be coming to me instead of the other way round."
                moxie "They sure will, men are super popular on dating websites."
                mc "It'll take me a long time to get used to that."
                moxie  "Heh, are the women in your world different or something?"
            "That's scary!":
                show moxie closeshy with dissolve
                moxie "I’m afraid you’ll be fetishized, perhaps even objectified to a degree. If anyone doesn’t treat you right, you’re well within your means to leave the situation."
                moxie "You shouldn't be scared though. Don't you humans have heat?"
        mc "Heat simply isn’t a thing in my species."
        show moxie closeembarrassed with dissolve
        moxie "Your human women don’t experience heat at all? I didn't realize that!"
        moxie "I’ll try to explain it then, might save you some trouble."
        show moxie closealthappy with dissolve
        moxie "You said you felt unusually aroused last night, right? That'll be due to pheromones."
        show moxie closehorny with dissolve
        moxie "Due to these pheromones, if you’re alone with a mare in heat for a long enough time, the impulse for sex will grow. It’s biologically wired that way."
        mc "Biologically wired? Why? That seems a bit intense."
        moxie "Intense perhaps, but heat is heat, it's evolved to be like that."
        moxie "Arousal signals keep pinging back and forth between the male and female like a feedback loop."
        moxie "It’ll keep going until you’re both unbearably aroused. And trust me, these girls are already unbearably aroused, because there’s not a whole lot to go around…"
        "I can't entirely tell if Moxie's explaining the science or her opinion, but there's something that doesn't quite sit right with me about this whole situation."
        "I finally realized I've been overlooking something quite simple ever since I arrived."
        "I haven’t seen a single other male creature, which is a particularly important crux of this conversation."
        mc "Moxie, I need to ask. I haven’t seen a single male, where are they?"
        show moxie closealthappy with dissolve
        moxie "Hm? I’m assuming they’re in the same place as your world, scattered about here and there, they’re just a lot rarer than the females."
        mc "Rarer? No, actually there’s a 50/50 split where I’m from, so that is quite shocking to discover."
        show moxie closeshocked with dissolve
        moxie "Ahh, damnit, I keep making assumptions about you and humans... You really are different."
        show moxie closesad with dissolve
        moxie "Alright, so, males here are relatively a lot rarer. Maybe a 15/85 split, and that split varies between species apparently, I don’t know."
        moxie "The point is, there’re not enough stallions to go around."
        mc "That’s so weird… Why are the males so rare? That seems paradoxical from an evolutionary perspective."
        show moxie closeneutral with dissolve
        moxie "Right? I was curious myself, so Penny lent me some books on the subject, and I’ve done some reading."
        moxie "According to one biology book, we were evolved from an alpha male system where a single male would copulate with a herd of females."
        moxie "I have to assume that through natural selection females that birthed more female young were the preference."
        mc "It sounds like our species have slightly different biology then, that’d be impossible for humans."
        mc "Anyway, alpha male? Sounds kind of scary, does this suburb have an alpha male that impregnates all the mares?"
        show moxie closelaughing with dissolve
        moxie "Haha, no, absolutely not. That herd mentality died many millenia ago. We've since developed society and culture. Monogamy is seen as desirable in the modern age."
        show moxie closehappy with dissolve
        moxie "A lot of mares actually have the dream of falling in love with their one and only. I must admit, I can see why the idea of being singled out among so many mares is appealing."
        show moxie closeserious with dissolve
        moxie "Although the reality is that stallions are in such hot demand, they’re often the ones being swept off their feet by rich and attractive mares, because being married is seen as an extravagant status symbol."
        moxie "I assure you all the richest mares have husbands."
        mc "So… What do all the lonely mares do? Seems pretty awful."
        show moxie closehappyneutral with dissolve
        moxie "Nah, not as awful as you might think."
        moxie "Many have life-long relationships with other mares… I think Penny will do that when she’s older."
        mc "Ah, a fair few lesbian relationships, then?"
        show moxie closeneutral with dissolve
        moxie "Lesbian? I haven't heard that word in a long time, we don't tend to use words like that to describe people."
        moxie "Most mares like both sexes, including myself. As such they're not really considered 'lesbian' relationships, they're considered normal."
        moxie "You also have to consider interspecies relationships, of which there is no stigma."
        mc "Pardon my ignorance, but how aren’t you going extinct? If monogamy is the standard, then even if every couple is having 2 to 3 children the overall population is at a loss."
        show moxie closelaughing with dissolve
        moxie "Ah-hah! So, you are paying attention. A lack of breeding is no small problem, but the issue has been alleviated by the magic of unicorns. Unicorns are the founders and upholders of pony society."
        show moxie closehappy with dissolve
        moxie "Unicorns have ways to artificially inseminate mares, multiple ways! Every mare has the opportunity to have a child. Not everyone does, but it gives our population of 25,000 a healthy steadiness. No overpopulation or underpopulation."
        "25,000... Wow, is that really all?"
        moxie "It’s not unusual to see a single mare with a child, like my mother, or a mare couple with a child."
        mc "That’s amazing, I wish the problems of my world could be solved with a swish and flick of a wand, or horn."
        show moxie closealthappy with dissolve
        moxie "I know! I love magic, I'd love to show you a thing or two so you can see how wonderful it is."
        mc "I’ve always daydreamed about being able to do magic. I guess I won’t be the one doing it, but this is like having my fantasy become a reality."
        show moxie closelaughing with dissolve
        moxie "Then what are we waiting for? My wagon is only across the river, let’s go!"
        show moxie laughing with dissolve
        "Moxie grabs my hand and we both jog to her nearby wagon."
        hide moxie laughing with None
        scene bg black with dissolve
        stop music fadeout 5.0
        stop ambience fadeout 5.0
        "…"
        play music wagon fadein 5.0
        scene bg moxiewagonday with dissolve
        "Moxie reaches for a shelf, and since she’s a little on the short side, she has to get on her tippy toes to reach."
        "She huffs adorably as she lifts down a spell tome. I figured she'd have a magic spell to make that easier, but what do I know?"
        show moxie happy with dissolve
        moxie "Okay, this one has lots of fun things! This is a magic fun book; it has a couple of simple spells in here for entertainment."
        "Each spell in the tome has a double paged spread, a picture, some instructions, and some tips for utilisation and casting. It’s like a recipe book for magic. Unlike a recipe book though, there are no ingredients."
        "Come to think of it, the book does seem rather juvenile, as if it's aimed at younger audiences."
        mc "Hey Mox, I have a question: can any unicorn just cast a spell without preparation or ingredients? Isn’t there a law of equivalent exchange?"
        show moxie althappy with dissolve
        moxie "I’m not the best person to ask, you should’ve asked Penny while you had the chance."
        moxie "I’ve only read a little bit on the theory, but any Unicorn can cast a spell if they learn how to do it. However, they have a limited pool of magical power that they draw from."
        moxie "No external ingredients are required, but you only have so much magical power, once that's gone you feel exhausted and sleepy."
        moxie "You can regenerate magical power by sleeping or eating, so in some ways, there may ultimately be some kind of equivalent exchange as you say. Heh, talking about this makes me feel like a nerd."
        show moxie happy with dissolve
        moxie "Oh, and ponies have varying magic 'pool' sizes; it’s like a muscle, it can get bigger!"
        "I snap my fingers triumphantly as I have my own little realisation, it’s just like mana from a video game."
        "I wonder if they have video games in this world. There are so many random interesting things that may or may not be here that are subtly different to my world. "
        "I know Moxie has a radio, and I think she has a laptop too."
        "Didn't she mention dating websites earlier? Either way, I'm getting sidetracked."
        mc "Okay, how’s your mana, can you show me a few spells?"
        show moxie happyneutral with dissolve
        moxie "Mana? You mean my magic? Well, I certainly can, there are plenty of small spells we can mess around with. Here’s one I can do off by heart, this is a classic!"
        stop music fadeout 7.0
        show moxie smug with moxiespell
        play sound magic1
        "I watch eagerly and lean in as I see the purple aura around her horn stir, it maintains its glow for a while, but nothing appears to happen."
        "I sit there with growing confusion as Moxie returns a smug look."
        "In the corner of my eye I see movement..."
        "Upon turning to see, a floating stuffed bunny rabbit from the shelf falls right onto my lap!"
        play sound movement
        show bg moxiewagonday with vpunch
        mc "Wow! Telekinesis, right? That’s awesome, I’ve always wanted to do that."
        show moxie laughing with dissolve
        moxie "Ahah, I know, pretty awesome right? That one has a pretty severe weight and distance limit. To be honest, I wouldn’t even be able to lift up this spell book at my current level."
        "That explains the lightweight bunny rabbit as her choice of object."
        show moxie happy with dissolve
        moxie "Still, you gotta love being able to write things down using telekinesis, it’s a dream when you’re doing a task that requires three hands. Or if you’re lazy and don’t want to reach for something!"
        mc "You’ll make me jealous, and we’re only on the first spell! What else is there?"
        show moxie happyneutral with dissolve
        moxie "This book is full of silly things: like changing the pitch of your voice, changing the colour of your hair, or giving yourself cat ears."
        moxie "They’re all temporary though, the laws around magic can be strict."
        mc "That makes sense, you wouldn’t want a unicorn changing their identity and framing someone else for a crime."
        show moxie neutral with dissolve
        moxie "Uhh, heh, something like that!"
        show moxie happyneutral with dissolve
        moxie "Anyway... If you recall I’m a street magic performer so I know all sorts of dumb tricks, although I won’t be shooting off any fireworks inside my wagon."
        play music challenge fadein 3.0
        $ pmhc = 0
        $ pmap = 0
        $ pmtg = 0
        label day27:
            if pmhc == 1 and pmap == 1 and pmtg == 1:
                jump day28
        menu:
            moxie "Pick out some spells and I'll do 'em."
            "Change your hair colour." if pmhc == 0:
                $ pmhc = 1
                moxie "Easy peasy, watch this."
                play sound magic1
                show moxie blonde with moxiespell
                mc "Woah, it's like you instantly dyed your hair!"
                moxie "Don'cha think blondes have more fun?"
                "I brush my fingers through Moxie's hair, it's incredible."
                show moxie shy with moxiespell
                moxie "Awh man, these spells really don't last very long."
                mc "Why does a spell as simple as changing hair colour last such a short time?"
                mc "People dye their hair all the time where I'm from."
                moxie "Magic is kinda complicated. My hair may have looked dyed, but perhaps it was just a temporary optical illusion."
                moxie "Perhaps my hair was indeed dyed; coated with a blonde colour, or the molecular composition of my hair changed."
                moxie "It's hard to say, but there are better ways to dye your hair than a spell."
                mc "Right, I think I understand."
                show moxie althappy with dissolve
                jump day27
            "Change your appearance." if pmap == 0:
                $ pmap = 1
                show moxie happy with dissolve
                moxie "Oh? You want me to do that? If only..."
                moxie "It's a really tough one, most ponies can't even do this."
                moxie "I have to visualise someone in my mind as accurately as I can. Although, I suppose it doesn't matter if I botch it slightly."
                moxie "I could try Penelope, I know her inside and out, hehe. Okay, here goes nothing."
                play sound magic1
                hide moxie with qd
                show penelope happy with moxiespell
                moxie "Hoi dere I'm Penelope, how do I look?"
                mc "Woah, that's almost perfect!"
                "Moxie looks down at herself and shrugs"
                show penelope laughing with dissolve
                moxie "Hehehe, it's my speciality!"
                hide penelope with qd
                show moxie happyneutral with moxiespell
                moxie "Doesn't last very long either; like we said earlier, 'magic crimes'... Those royal sisters sure are strict..."
                mc "Can't people just do a spell that lasts longer?"
                moxie "Yeah sure, but it's hard to find. In the same way dangerous chemicals are hard to procure, dangerous spells are too."
                mc "That makes sense."
                jump day27
            "Turn me into a girl?" if pmtg == 0:
                $ pmtg = 1
                $ turnedintogirl = 1
                show moxie smug with dissolve
                moxie "Well aren't you daring."
                mc "It's one of those things you're always curious about, right? What's it like being the other gender?"
                moxie "I don't think you're missing much. Ready for your ten seconds of wonder?"
                mc "Wait, hang on..."
                play sound magic2
                show moxie laughing with moxiespell
                "Before I can get a word in, my body feels instantly modified."
                "I was concerned because I thought gaining and losing body parts would be a painful process, but rather I didn't feel anything at all."
                "I looked down and I could indeed see a pair of breasts, and there was nothing inbetween my legs. But I could still feel my male genitalia, as if it was a phantom limb."
                mc "Okay, this feels-"
                mc "O-Oh? My..."
                show moxie happy with dissolve
                moxie "Ahaha, even your voice went girly, I honestly wasn't expecting that."
                mc "D-Don't take too much joy in this."
                mc "This feels weird... Why is a spell like that in this book?"
                moxie "Temporary gender changing spells are one method mare couples use to have children, it's somewhat normalised here."
                moxie "This is a really short length variation though, made even shorter by my weak magic."
                show moxie happyneutral with moxiespell
                moxie "There we go."
                mc "Oh man... Let's never talk about this again"
                show moxie laughing with dissolve
                moxie "You got it, boss."
                jump day27
            "That's all. (Proceed)":
                jump day28
        label day28:
            pass
        show moxie smug with dissolve
        moxie "Now for the finale, I want to show off a bit."
        moxie "Eh hem, watch in awe as the Super and Amazing Moxie performs the most spectacular feats of magic ever witnessed by your alien eyes!"
        play sound magic3
        hide moxie smug
        show purple
        with moxiespell
        hide purple with s
        "Moxie begins casting a spell and immediately my vision is clouded by a puff of smoke. It’s not an unpleasant smoke though, it smells like lavender and it quickly disperses. Moxie was gone, she has vanished!"
        "Actually, no, Moxie had just moved to stand behind me, I heard her footsteps."
        show moxie smug with dissolve
        "I turn around to face her, it may have just been a cloud of smoke trick, but she still conjured the smoke, so I'm impressed."
        moxie "Ehehe, I think you saw through my smoke cloud, but fear not! For the Great Moxie is practicing invisibility magic which will drastically improve my stage performance."
        moxie "Witness!"
        play sound magic2
        show moxie transparent with moxiespell
        show moxie transparent2 with dissolve
        show moxie transparent with dissolve
        show moxie transparent2 with dissolve
        show moxie transparent with dissolve
        "While casting this next spell, Moxie exerts herself a little, as if lifting a weight. Her body then flickers with some translucency."
        "She doesn’t fully go invisible, I can see right through her, leaving me utterly stunned by the display."
        show moxie sad with dissolve
        moxie "Gahh… hahh, that’s a tough one... I’ll do it one day, just you wait!"
        mc "Incredible!"
        stop music fadeout 10.0
        show moxie neutral with dissolve
        moxie "You really think so? Even though I couldn’t do it…?"
        mc "Of course, as I said earlier, I could only dream about magical powers, yet here you are doing all these amazing things."
        show moxie althappy with dissolve
        moxie "Oh please, you’re only saying that because you’ve never seen magic before. I’m really... really not that impressive… I'm actually pretty damn awful at magic..."
        mc "That doesn’t make it any less impressive, if anything, your hard work and dedication makes your effort truly admirable. "
        hide moxie althappy with dissolve
        show moxie closesatisfied with dissolve
        "She surprises me with a tight hug."
        show moxie closehappytears with dissolve
        moxie "You have no idea how much I appreciate hearing that."
        mc "It's true though, you really are amazing."
        moxie "Penny said something similar to me when we first met."
        moxie "She looked out for me, helped me through a difficult time, and we became best friends."
        mc "A difficult time?"
        show moxie closetears with dissolve
        play music sad2
        moxie "I came from a town that had a small ratio of unicorns to regular ponies, so I was arrogant when I was growing up."
        moxie "I thought I was on top of the world."
        moxie "It was only a few months ago I came to Arcadia to do a performance, and in my hubris I caused a serious incident that Lily and Penelope had to fix."
        moxie "I learned humility through that incident, it was a reality check."
        mc "What happened?"
        moxie "I had a caged Ursa I wanted to show off in my performance, but I agitated it too much, and it escaped into the suburbs."
        moxie "The only reason I had the creature caged is because I kidnapped it while it was asleep, which is horrible enough in retrospect, but also... I wasn't powerful enough to actually stop it once it escaped."
        mc "Lily and Penelope had to stop it?"
        moxie "Meh... I'd rather not go into detail."
        mc "Alright, you don't have to tell me if you don't want to."
        moxie "Lily scolded me ruthlessly, but Penny, she forgave me, that girl has a heart full of empathy."
        moxie "Penelope recognized that I felt utterly awful, I was sobbing, reality had come crushing down on me all at once. My pride had put peoples' lives in danger."
        moxie "She reached out to me, picked me up, dried my tears. Showed me kindness, friendship and love."
        moxie "She also introduced me to a new world of magic and possibilities."
        moxie "I had spent all my life strutting around as if I was special, just because I was born with some shitty magical power."
        moxie "I thought I was goddess' gift to the world, so I neglected to build my character and mature."
        moxie "All I ever really wanted to do was feel special. To feel like I had a place in the world."
        moxie "But when you have a toxic personality, you push people away; they stop caring and they distance themselves from you."
        moxie "One by one you’ll lose all your friends."
        moxie "Before I realized I was pushing everyone away, I was alone."
        moxie "When you have a toxic mindset, even then you tend to look back at your old friends with resentment."
        moxie "I'd think things like 'I'm too good for them', or 'they betrayed me'."
        moxie "But, heh, it all seems so ridiculous now, I was the asshole the entire time."
        show moxie closehappytears with dissolve
        moxie "When I met Penny, I had a profound realisation; I didn’t need to show off, brag or one-up to be special. All I needed to do was make people happy and fill their day with cheer and excitement."
        moxie "That wasn’t all though, Penny helped me improve my performances and magic by lending books and encouraging me to study."
        show moxie closetears with dissolve
        moxie "Truth is, I wasn’t very good at magic, I’d always assumed I was though."
        moxie "My pride prevented me from studying and truly bringing out the best I could be."
        moxie "Penny told me I needed to start being more open minded, so..."
        show moxie closehappytears with dissolve
        moxie "I started studying new magic, and I radically altered my shows to be more light-hearted and entertainment focused."
        moxie "It's incredibly cathartic to finally learn a new spell after trying so hard, and to see people genuinely enjoying my shows."
        moxie "I’d finally found my place in the world, and it wasn’t through bringing other people down with negativity, it was about lifting them up with positivity."
        show moxie closetears with dissolve
        moxie "Sorry, I'm crying..."
        mc "It's okay..."
        moxie  "I didn't expect to get so emotional over this, I feel silly now."
        moxie "*Sniff*"
        show  moxie closehappytears with dissolve
        moxie "I’ve seen beauty in Arcadia. I’ve decided I want to study magic at the university here."
        moxie "It’s daunting, and I know it’ll be the hardest thing I ever do in my life, but that’s what I want to do."
        moxie "I would like to say that I’m different now, I’m working harder, studying diligently and keeping my ego in check, but I know there's a long road ahead of me."
        mc "I wish you the best of luck, Moxie."
        moxie "Thank you [playername]… I can’t say what the future holds for me, I don’t know if I’ll always be a magical performance artist, but I know now that I want to spread happiness."
        moxie "*Sniff* Can we cuddle?"
        mc "Of course."
        hide moxie closehappytears with dissolve
        stop music fadeout 12.0
        play ambience ambienceday fadein 5.0
        "She finishes talking and slumps into my chest, her mane sweeps over her eyes and we just lay there together. I could have said something at that moment, but I knew Moxie just wanted to cuddle. I stroked her hair and just enjoyed the moment."
        "I peek down at her, trying not to move my head too much as to avoid disturbing her. She doesn’t seem to be crying, quite the contrary, she’s smiling."
        "I take a deep breath, lay back into the sofa and close my eyes."
        show bg black with dissolve
        "Bless her, she's trying so hard."
        "She's so beautiful inside and out."
        "My mind starts wandering, Moxie, Penelope, this world..."
        "The realisation that this is my new life hasn't fully set in yet. I still check the clock and think 'I have class soon'."
        "Although I am finally starting to get more comfortable in this world, particularly with one of the largest cultural differences: the lack of clothing."
        "Previously I saw nude women in a sexual light, but in this world, nudity is normalised."
        "I’m surprised by how easily I was able to adapt to that. Less and less I look at nude mares walking past in a sexual manner, I'm starting to just see it as their natural state."
        "This is probably what it's like visiting a nude beach; initially a shock, yet the mind adapts."
        "However... Moxie has been different to me, there’s something special about her."
        "When I look upon her form, I see a distinct beauty and sexuality."
        "I've only known her for a day, but she's more than just a stranger. She’s a friend, maybe something more. It feels like I’ve known her for years."
        "I like her confidence, her brash attitude. She says what she thinks and won’t hesitate to put me in my place if necessary, I like that in a girl."
        "But she also has that softer side, she has a charming innocence and shyness when she lets her guard down, it makes her incredibly endearing."
        "The sex deal is a surprise too, now that I've gotten to know her more it almost goes against her personality, but maybe that's because I'm viewing it from my own human standards and not pony standards."
        "Moxie wasn't wrong when she mentioned pheromones, I definitely feel unusually horny after being around her all day."
        "Right now, the mere thoughts of arousal and libido are causing me to stiffen, it’s like my dick was ready to immediately go at the slightest hint of sexual thought."
        "Moxie may have her eyes closed, but I wonder if she feels something too?"
        "She’s in heat, so she’s naturally in a state of high libido, no doubt pent up too. If my trail of thought is right, then being around me all day is only going to make her even hornier."
        "Even now just cuddling together, I can feel my building arousal. It’s her heat, it arouses me, and in turn, my arousal only furthers her own..."
        "It's just like she said, it's a feedback loop, I can feel it right now as we're cuddling. I can feel it pinging."
        show bg moxiewagonday with dissolve
        show moxie boobs with dissolve
        "I can't help but open my eyes and glance at her impeccable body."
        "I become aware of her fidgeting; she stifles a moan; she can feel it too."
        hide moxie boobs with dissolve
        "I didn’t even notice myself become unbearably erect. My sense of time is askew, time is moving so fast, yet my senses are so heightened I feel everything so slowly and acutely."
        $ introdoggystylereplay = 0
        label introdoggystyle:
            pass
        show moxie closehorny with dissolve
        "She opens her eyes for the first time in a while, and the abrupt sight of my erection beside her doesn’t even phase her."
        stop ambience fadeout 5.0
        play music sex1 fadein 30.0
        show moxie closehorny with dissolve
        moxie "Mm, I could feel the pheromones, even with my eyes closed."
        hide moxie closehorny with dissolve
        "I can see her biting her lip as she peers at my manhood, she extends her hand and jacks it a few times before standing up and closing the window."
        scene bg moxiewagonlamp with dissolve
        show moxie horny with dissolve
        moxie "Gosh, you’re like a drug, you know that [playername]? I’ve been horny all day, but what I’m feeling right now, this second, it’s something else."
        mc "I’ve felt the same too."
        moxie "Ohh, you have? Look closely."
        hide moxie horny with dissolve
        show moxie butt with dissolve
        "Her tail starts swishing back and forth while she bends over, slightly exposing her rear to me."
        moxie "I’m so horny right now, I’d let you do anything to me."
        "I haven’t had much of an opportunity to get a good look at her ass, especially with her tail in the way."
        "It’s a cute bubble butt, and as her tail swished, I’d occasionally get a peek between her thighs."
        moxie "I want to fuck you… I really want to fuck you."
        moxie "Even though it’s my first time, I want it to be with you…"
        "She’s so wet, I can see a trail of grool connecting her pussy and inner thigh. "
        "I can’t hold back any longer, I start masturbating and Moxie licks her lips as she watches."
        moxie "Ahhh, I simply can’t wait any longer… Please, come to my bedroom and ravish me."
        hide moxie butt with dissolve
        "With that, she takes the lead, walking into her bedroom. I hastily follow behind her, my erection swaying in tow."
        scene bg moxiebedday with dissolve
        show moxie butt with dissolve
        "When I arrive in her bedroom, I’m greeted to the gorgeous sight of Moxie presenting herself to me."
        moxie "Close the door behind you, love... I’m going to get really noisy."
        "With a click, the wooden door shuts, leaving us in a room lit only by the light penetrating the closed blinds, it shimmers over Moxie’s rump accentuating the roundness of her bubble butt."
        "I crawl on to the bed, getting on my knees behind her and watching as she playfully wiggles her ass back and forth."
        moxie "Even though this is my first time, I’m pretty excited, and not just because I’m in heat."
        moxie "I feel really comfortable giving my first time to you. I know it doesn’t mean much, it’s just sex at the end of the day, but I know how important it is to feel comfortable with your mate."
        mc "I’m glad we’ve managed to bond so strongly, even in such a short time."
        show moxie buttmoan with dissolve
        moxie "Guess we’re just meant to be, right? Hah… Don’t listen to me, I’m too horny to think sensibly right now, I’d probably say yes if you proposed."
        "I bring both of my hands to her ass; I squish and squeeze it. It’s soft and the fur indents when I apply pressure with my fingers."
        "Now that I’m behind her, I get a close up look of her pussy."
        "Some of the tufts of fur are sodden and damp, her pussy is in an extremely aroused state; it’s slightly swollen, so wet it’s shiny and a little drippy too."
        "I bring one of my fingers to her pussy to see how it feels; it’s warm to the touch and I can feel her natural lubrication on the tip of my finger. Moxie coos in reaction to my touch."
        moxie "Oooh, getting adventurous? Rub my clit, that feels best."
        show moxie buttclitrub with dissolve
        "I start to gently rub her clitoris back and forth; Moxie reacts extremely favourably by muffling moans and stirring about on top of the bedsheets. Her toes even start wiggling in the corner of my eye, that’s adorable."
        moxie "Ahh… For some reason, it feels so much better when you touch it…"
        "I use my thumb, pressing it on the clit and moving around in circular motions. I’m no expert at sex, but I’ve seen enough eroges and porn to know how to really get a girl going."
        "On second thought, maybe I should use my tongue, she really liked that yesterday. I pull my hand away and shuffle closer between her furry thighs. Moxie seems to tense up a little as she no doubt guesses what I’m about to do."
        show moxie butttongue with dissolve
        "I stick out my tongue with a rough trajectory of her clit and close my eyes. I was going to use my hands to bring her butt closer, but she gently moves back and presses herself against my face, cheeky!"
        "I wiggle my tongue around, aimlessly at first, but I get a feel for her vulva and find the nub shape of her clit where I began to lick circles on top of it, occasionally swiping side to side."
        moxie "W-Woahh… Ahh… Your tongue is great..."
        moxie "Mmph… Keep going, that feels really good…"
        "Tension seems to dissipate in Moxie as her body completely gives into the pleasure of my tongue."
        "She tries to hold back a continuous flow of moans, perhaps out of embarrassment, but my tongue continues unrelentingly and soon she is unable to contain herself."
        moxie "Nn… mm… Aahhh! Mm. Aahh…"
        "My tongue starts to quickly swipe left and right against her clit, I noticed she seems to get the most pleasure from this, although it does tire my tongue out the fastest."
        "The pleasure overwhelms her slightly and her ass starts to squirm a little."
        moxie "Mmphh, y-you’re going to make me… Ahh!"
        "I have to hold her ass in place as she wriggles under the touch of my tongue, her body shivers as she starts to orgasm."
        moxie "C-Coming! "
        "I keep pleasuring her with my tongue through her entire orgasm, she moans with glee throughout."
        show moxie butt with dissolve
        "As Moxie begins to relax, I pull back. My tongue is aching, I hadn’t anticipated it being so difficult, but I’m glad I managed to make Moxie feel so good."
        moxie "*Pant* *Pant* I-I didn’t expect you to do that…"
        mc "I’m not done with you yet."
        show moxie buttclitrub with dissolve
        "I think she’s even wetter than she was before, which is impressive, there’s even some grool oozing out of her. I bring my finger up, rubbing inside her vulva as I do so."
        moxie "Mmphh… Even now, you feel the need to tease me?"
        mc "You’ve seen that my dick is pretty big; I need to make sure you can take it. It’s your first time after all."
        show moxie buttfinger with dissolve
        play sound cum
        "I pry a little at her entrance with a finger, as I apply a little pressure, it slips in deeper with ease. Despite that, I can still feel a distinct tightness around my finger."
        moxie "Mm… That feels good… I’ve played with myself plenty before, it shouldn’t be too tight…"
        "Moxie’s body trembled as I moved my finger back and forth, I've heard there are a few particularly sensitive parts in the vagina such as the g-spot, so I tried applying pressure along her insides."
        moxie "Ahh! Woah!"
        mc "Is this okay? You’re trembling a little."
        moxie "Ahah, it’s not like it hurts, don’t worry. I was just a little surprised."
        "Her wetness coats my finger helping it move readily inside, I can even feel her loosen up ever so slightly."
        show moxie doggystyle1 with dissolve
        moxie "Mmm, ahh… C-Can you do it with your…"
        "She doesn’t finish her sentence, but I know what she means. It’s not like Moxie to mince her words. I guess even she can feel shy at a time like this."
        show moxie doggystyle2 with dissolve
        "I slip out my finger, it's so wet it's practically dripping, humans definitely don’t get this wet."
        show moxie doggystyle3 with dissolve
        "I bring that same hand to my cock and guide it to her pussy, pressing it against her entrance."
        play sound cum
        "I was going to insert myself carefully but before I knew it, she pressed her rump into me and succeeded in taking my entire shaft effortlessly."
        "She let out a moan and arched her back in response to the spike of pleasure. One of her hands was clinging to the bedsheets, while the other was fervently rubbing her clit."
        moxie "Mm… Ha… It feels so big... Gosh damn... *Pant*"
        play ambience sex
        "The grip around my dick was tight, it felt extraordinary, the warmth and wetness stimulated me and overwhelmed my senses. I bring both of my hands to her hips, use them as leverage and begin to thrust."
        "My movements are slow and clumsy at first, I have never moved my body like this, so it’ll take a while to get used to it."
        "The sensation of her pussy clinging to me was euphoric, her insides throbbed and squeezed my member, pleasing each inch."
        show moxie doggystyle4 with dissolve
        moxie "Ahh, mmm, this is better than I even imagined…"
        "I agreed, her pussy felt unbelievable, almost too good. So good that if I went too fast I might cum too soon, and I want to make sure I enjoy my first time for as long as I can."
        "I can’t forget that this is just as much for her as it is for me, perhaps even more for her since she’s in heat."
        "I decided to pace myself and fuck her gently. My thrusts came slowly yet they went deep. I could feel her body react favourably, especially when I got deep inside her. I must be creating friction against some sensitive spots."
        show moxie doggystyle5 with dissolve
        moxie "Aaaaaaaaahhhhhhhhhh… Hahhh, hah… This is mind numbing."
        "Her constant cute moans were arousing; I really want to get her off again, so I try to focus my thrusts deep within her where it’s most pleasurable."
        moxie "Mmm-mmm! Y-you’re! Ahh…"
        "A sentence tries to escape Moxie’s mouth, yet it fails, replaced with her moans. Earlier it wasn’t hard to make her come with my tongue, I was sure she was already close again as her reactions started to mirror those from before."
        moxie "Ahhh… Mmm.. I- ahhh… C-Coming!"
        "I keep fucking her deeply as she climaxes, her insides tighten around my shaft and my cock throbs in response."
        moxie "Mmm, ahh… [playername]!"
        "I didn’t want to hold back anymore. I want to fuck her as hard and as fast as I can."
        "I began to lose myself in the moment, holding her hips firmly as I sped up my thrusts, slamming faster and harder into her soppy wet pussy."
        moxie "Nn… Mmm… Faster! "
        "I think her climax just ended, but she shows no signs of slowing down. She starts bouncing her ass into me, matching the rhythm of my thrusts, creating a satisfying slapping sound each time our bodies come together."
        "Her pussy felt immensely pleasurable and the faster I go the better it feels."
        "Every individual sensation was better, I could feel pleasure surge through my body as her insides continued to squeeze around my shaft, massaging every inch. "
        "I could tell that my orgasm was inevitable, but even so I tensed my cock and held back exploding inside her so I could savour each second of this immense pleasure. "
        moxie "*Pant* I want… Ahh… I want you to come inside me!"
        "Her lewd words spurred me on, the moment I let down my guard my orgasm rapidly welled up within me. My mind filled up with white and before I knew it, I reach the point of no return. "
        play sound cum
        show moxie doggystyle6 with cum
        play sound cum
        show moxie doggystyle6 with cum
        "My cock throbbed and my muscles tensed as I shot my thick, hot load deep inside of her tight pussy and I don’t stop fucking for a second throughout my entire orgasm."
        "It felt far too good, in fact it was the best thing I’d ever felt, and I wanted to savour each and every thrust. "
        play sound cum
        show moxie doggystyle6 with cum
        play sound cum
        show moxie doggystyle6 with cum
        "I kept cumming, three loads, six loads, nine loads, more than I knew possible, each and every drop firing deep inside her. "
        show moxie doggystyle7 with dissolve
        "Some of the semen leaks out of her and drips down, contrasting against her cool blue thighs. "
        show moxie doggystyle8 with dissolve
        stop music fadeout 14.0
        stop ambience fadeout 1.0
        play ambience ambienceday fadein 15.0
        "As I pull out, more oozes out and as if suddenly released from a constraint, Moxie falls down onto the soft covers in a state of overexcited panting."
        show moxie closesatisfied with dissolve
        "She rolls over after a few seconds and gestures for me to come closer, so I crawl up to lay beside her."
        "I can feel her arm wrap itself around me as she pulls me closer into a cuddle. I indulge in her touch, her softness and warmth against my bare skin. It’s exactly what I need after sex."
        show bg black
        hide moxie
        with dissolve
        $achievement.grant("Achievement01_Moxie")
        init:
            $achievement.register("Achievement01_Moxie")
            $achievement.sync()

        $achievement.sync()
        if crystalballactivated == 1:
            $ crystalballactivated = 0
            jump cbmenu
        "I close my eyes and bring one of my arms around her furry back and embrace her too, we snuggle together silently as we recompose ourselves."
        "Cuddling naked with someone so soft, so fluffy, this is almost as good as the sex."
        "We lay together for quite some time, just enjoying each other’s company. Moxie is the first to break the silence."
        moxie "How was it? Your first time?"
        mc "It was amazing, I’ve never felt anything even close to that."
        mc "Being stuck in this world might not be so bad after all."
        moxie "Ohh… Being stuck? Yeah..."
        show bg moxiebedday
        show moxie closealthappy
        with dissolve
        mc "How was it for you?"
        show moxie closesatisfied with dissolve
        moxie "I’m still high in the clouds, floating, floating. My brain is scrambled, my toes are twitching. "
        moxie "I’ve masturbated before, of course I have; I do that even when I’m not in heat."
        moxie "My usual orgasms are about five or six out of ten… It’s nice enough to warrant doing it at all, and my orgasms are a little more powerful during my heat, let’s say eight or nine out of ten."
        mc "A rating out of 10? What would you rate your orgasms just now?"
        show moxie closesmug with dissolve
        moxie "Honestly? About one hundred, especially the third one, all I could see was white, I think I blacked out, actually no, I think I whited out. I still feel tingly."
        "Did she just say she came three times? I only counted two! Wait, she said third, not last…  Did she come more than three times? "
        mc "Even though that was the best I've ever felt, it sounds like your orgasm was transcendental. Maybe there's a spell that can make my orgasm feel that good."
        show moxie closesatisfied with dissolve
        "She leans in and smooches me on the lips, there was a little bit of tongue from her too, but the kiss is short-lived. "
        show moxie closesmug with dissolve
        moxie "You know what this means right?"
        mc "What's that?"
        show moxie closelaughing with dissolve
        moxie "I'm gonna want more, lots more!"
        mc "Hoh boy, easy there, bunny."
        show moxie closealthappy with dissolve
        moxie "I could tell you put in a lot of effort to please me, thank you for that, you made my first time special, really special."
        moxie "You didn’t have to do that; I would have been satisfied anyway because of the heat."
        mc "I thought I’d try my best to please you, that helps satisfy your heat, right? That’s why you made the deal. I enjoyed it a lot too, it wasn’t an entirely selfless choice."
        show moxie closesatisfied with dissolve
        moxie "The deal… Even so, I was surprised that you decided to go above and beyond…"
        moxie "That was thoughtful of you…"
        moxie "Next time I’ll be sure to return the favour."
        play music wagon fadein 10.0
        show moxie closehappyneutral with dissolve
        "I can feel her fingers walking their way down my back, her voice had a seductive tone to it."
        "She’s already planting the seed of our next sexual encounter in my mind; I’m looking forward to it."
        show moxie closeneutral with dissolve
        "I keep a close eye on her expression, for a brief moment she seems conflicted."
        moxie "Were you were just keeping your end of the bargain… Or was it something else?"
        mc "Hmm? Something… else?"
        show moxie closebashful with dissolve
        moxie "Aha… No, it doesn’t matter."
        show moxie closehorny with dissolve
        moxie "Remember earlier when I said if a mare in heat is in close proximity to a male for long enough, she’ll start prospecting for sex?"
        mc "Yeah, I was thinking about that earlier."
        moxie "One of the reasons I wanted to tell you is because Penny suggested you get work, and that means you’ll be working close to some attractive mares…"
        mc "Ahh… I see what you mean."
        show moxie closelaughing with dissolve
        moxie "You gave me a damn good dicking, [playername], it'd be rude to keep that all to myself."
        show moxie closehappy with dissolve
        moxie "I’m sure if you get close to one of them she’d be open to trying something sexy."
        show moxie closelaughing with dissolve
        moxie "Ahaha. I had a small idea, tell me if this is too much but…"
        stop music
        play music challenge
        moxie "It’d be kinda funny if you slept with them all."
        mc "..."
        mc "WHAT?"
        mc "Am I really allowed to do that? "
        show moxie closesmug with dissolve
        moxie "Allowed? Are you kidding me? Of course you are, strut your stuff, you might as well while you’re here."
        moxie "These ladies are all lovely, you’d be missing out if you just kept yourself to me. "
        mc "You’re okay with that?"
        show moxie closeserious with dissolve
        moxie "Pfft, why are you asking me? We’ve known each other less than 24 hours, you can do whatever you want."
        show moxie closebashful with dissolve
        moxie "I feel bad for what happened, so I want to make sure you have as much fun as you can."
        mc "And the answer to that is sex?!"
        moxie "At least one girl is going to try and ask you! I bet Riku will, she's horny!"
        show moxie closesmug with dissolve
        "She suddenly rolls right on top of me, so close her muzzle is booping my nose."
        mc "Wha-?"
        moxie "Come on [playername], you’ll be stuck here a while, at least have some fun."
        show moxie closealthappy with dissolve
        moxie "Don’t have too much fun though, you’ll still need to come back here for me, okay?"
        mc "Mm… Okay."
        hide moxie closealthappy with dissolve
        "We kiss briefly, and she rolls back to her spot and stretches out before closing her eyes. "
        "Moxie is right, new world, new me."
        "Damn, was she serious when she said I should sleep with ALL of them?"
        menu:
            "I'll sleep with all of them!":
                moxie "Ay, that's the right attitude!"
                moxie "I could give you advice, hehehe."
            "Why would anyone want to sleep with me?":
                moxie "Should I be offended as someone that just slept with you?"
                moxie "Come on [playername], I already told you why someone would wanna sleep with you."
                moxie "You're cute anyway, you'll be a hit with the ladies."
            "It sounds too hard.":
                moxie "Trust me tiger, the only complications you're going to have is picking which girl to fuck on which day."
                moxie "The time and place of fucking is going to be harder to organise than the how and why."
        mc "Jeez Moxie, you're a riot."
        moxie "Hehehe."
        "I lay on my back and stare up to the roof."
        show bg moxiebedroof with dissolve
        "I still find her nonchalance about freely having sex with others unusual."
        "Is it really that easy? I always thought sex was a big deal, ‘the most precious experience you can share with a person’."
        "I always assumed it'd take a few weeks or months to build up to sex."
        "That’s not entirely true though, sex between non-lovers is common where I’m from too. And I did sleep with Moxie really quickly."
        "Although... Moxie kinda came onto me, I didn’t do much."
        "Will the other girls make the first move too? That would make things far easier."
        "Maybe it’s different in a society with such a scarcity of males. Maybe it’s like Moxie said, during mating season girls will seek out males more willingly and sex will just kinda fall on my lap."
        "That's what she said earlier, but... It sounds too ridiculous to be true. The women of this society are basically like the men of my society, how confusing..."
        scene bg moxiebedday with dissolve
        mc "Hey Moxie, why did you have sex with me? Or rather, why so easily?"
        show moxie closehorny with dissolve
        moxie "Strange question... I'm not an easy slut if that's what you think! You're my first... Did we go too quickly?"
        mc "I don't think that at all, I'm just trying to better understand the cultural differences."
        show moxie closehappy with dissolve
        moxie "Ooohh... I think I know what you’re alluding to; it’s usually not this easy outside of mating season."
        mc "Is that so? Could you tell me more about heat then? I know you mentioned it earlier, but I’m interested to hear how it affects you."
        show moxie closebashful with dissolve
        moxie "Heat is like… Heat is like a burning desire that plagues the mind. You feel empty, and I don't mean mentally, I mean physically empty, I want to be filled, by... You know, a cock."
        moxie "I can still work and do day to day activities just fine. But it’s worse at night when I have nothing to occupy my mind, all I can think about is sex."
        moxie "Apparently, it goes away with a good dicking, but that only satisfies for a few days, I’ll update you on whether that’s true or not."
        show moxie closehorny with dissolve
        moxie "I masturbate 3-4 times a day during mating season, once in the morning, once after work and two before bed, that usually keeps me in check."
        moxie "Outside of mating season I only need to do it once a night, so that’s quite a difference. "
        mc "Only 3 or 4? Sometimes I masturbate 3-4 times a day, I wonder if our libidos are similar."
        show moxie closesmug with dissolve
        moxie "Yeah well, maybe you're just a pervert."
        moxie "Season only lasts about a month mind you, and it’s the only time a mare can actually get pregnant. From an evolutionary perspective it’s very important."
        mc "These mares I’m going to work with, they’ll want to have sex with me then?"
        show moxie closehappyneutral with dissolve
        moxie "Yeah, they’ll want sex. Whether they want to do it with you, well, that depends on the kind of relationship you form with the lovely ladies."
        mc "Are there seriously no other males around? This seems far too good to be true."
        show moxie closelaughing with dissolve
        moxie "You’re still hesitant? Come on, you're just projecting insecurities at this point."
        moxie "There are few males in the Arcadian Suburbs and 99 percent of them are likely in a relationship with a very horny mare that’s ridden that dick dry."
        show moxie closehappy with dissolve
        moxie "Trust me, by the end of this month you'll be crawling back to this wagon with empty balls and a lifetime of sexual experience."
        mc "It’ll take me a while to wrap my head around that; girls approaching me, asking me on dates, wanting to have a fling with me."
        moxie" Ah don’t sweat it, cultural differences and all that."
        moxie "You’re lucky you’re not a stallion, you’d honestly not get nearly as much sex, maybe from some wannabe MILFs, but from younger ladies? No way, no one wants to get pregnant."
        show moxie closehappyneutral with dissolve
        moxie "With that all said, I’m going to let you in on a secret of how to get the sex you want."
        mc "There’s a secret?"
        show moxie closelaughing with dissolve
        moxie "Yuuup, kinda!"
        show moxie closesmug with dissolve
        moxie "If you’re genuinely interested in a certain girl, I recommend sticking around after you’ve both finished working, just for drinks and conversation."
        moxie "Trust me, your presence throughout the day will make their hormones weep, so once you two are alone they’ll probably ask you to satisfy them. As if it was a favour, no less, no more."
        mc "That sounds sinister, I think I would feel guilty doing that."
        show moxie closeshocked with dissolve
        moxie "Guilty?"
        moxie "Ah don't be. At the end of the day, everyone’s having fun. That’s what matters in the end."
        show moxie closehappyneutral with dissolve
        moxie "If one of the girls doesn’t want to have sex with you, she won’t, I’m confident of that."
        moxie "It’s not like we completely lack self-control, else incest would be a serious problem, but it isn’t."
        moxie "Don’t forget that we enjoy sex just as much as you, and we’re being equally selfish in our wanton primal fuckery."
        mc "Well, when you put it like that… Guess I’ll go with the flow and see how this world plays around with me."
        show moxie closesmug with dissolve
        moxie "Now you’re getting it."
        "She stretches outwards and then sits up beside me."
        show moxie closehorny with dissolve
        moxie "Hm, can you believe that it’s only early afternoon after all that? That means we have plenty of time before we go to sleep."
        mc "Early afternoon? Got any plans?"
        show moxie closesmug with dissolve
        moxie "To be honest, I may be waiting for your refractory period to end."
        mc "Wait, what?"
        moxie "Ahaha, you didn’t think I was done with fucking you just once, did you?"
        moxie "This time… I’ll be on top; you lay right there for me babe."
        hide moxie closesmug with dissolve
        "Damn, she wasn’t kidding about how horny she was."
        scene bg black with dissolve
        stop music fadeout 5.0
        "…"
        stop ambience fadeout 3.0
        play music emotional fadein 5.0
        scene bg moxiebedroof with dissolve
        "Moxie and I rut long into the afternoon, and then into the evening. We did take a break to eat pizza before we just kept going."
        "And then back to cuddling, to kissing, to sex, then back to snuggling and the cycle repeats itself like we're two horny rabbits."
        "We experimented with plenty of positions and even introduced some magic! There’re some spells that help men keep going after they’ve ejaculated a few times."
        "I keep finding out new and exciting things about the world; they have takeaways, pizza, music and radio."
        "We listened to sweet classical pony music as we made love long into the night."
        "I enjoyed Moxie’s company a lot, she’s fascinating to talk to, and provides a lot of insight and perspective."
        "Tonight was one of the best nights of my life."
        "If this is just the beginning of my new life, then I can't wait to see what else this world has to offer."
        "But all nights come to an end, and as I sit here cuddling Moxie under the blankets, my mind stirred with the events of the day, eventually coming to a stop as I slept."
        scene bg black with dissolve
        stop music fadeout 3.0
        if crystalballdayactivated == 1:
            $ crystalballdayactivated = 0
            jump cbmenu
        "…"
        scene bg moxiebedroof with s
        "My eyes open, it takes a few seconds to readjust but I can soon make out the star constellation above the bed. I've seen it before but hadn't really paid attention to it."
        "I wonder what kind of interest Moxie has in space and stars."
        scene bg moxiebedday with dissolve
        "I roll over to my side to look at Moxie."
        "But she’s not there."
        "I sit up, daylight is seeping into the room through the closed blinds."
        "I’m not sure what time it is, but I can hear a distant bustle outside."
        scene bg moxiewagonlamp with dissolve
        "I crawl out of the bed and step into the main room. It’s definitely empty, I spot a note clearly presented on the table though."
        scene bg moxiewagonday with dissolve
        "'Hey sleepyhead, figured I’d leave you to nap while I head off to do some performances. I got mail from Penny and you have the go ahead for working in all the places I mentioned.'"
        "'Also, Penny wrote that you can work with her too if you want.'"
        "'I’ll see you in the evening, be back around five, I’ll cook us something delicious."
        "There are some directions to various places scrawled on the note, humourously listed 'to-do', the innuendo not lost on me."
        "I fold it up and place it in a satchel Moxie had given me, so I don’t get lost."
        "Upon reading the letter I’m initially concerned that I might be late for my first day of work, although I see the clock and it’s surprisingly only 8:10am."
        "I even have enough time to shower, I used her shower yesterday and the water pressure feels great. For a wagon this place is surprisingly kitted out."
        "I should eat too, there’s some leftover pizza, perfect."
        "After my morning routine I grab the satchel with the to-do list, there's plenty of room in here to store the world's currency and various items."
        "And with that, I'm ready."
        "It’s intimidating to walk out to that brand new world on my own, to meet new people."
        "Intimidating, but I can’t help but feel excited too. I hope everyone is as pleasant as Moxie and Penelope."
        "Could I really start a new life here? Yeah, I bet I could."
        "Only question is where should I work today?"
        jump preworldmap


        return
