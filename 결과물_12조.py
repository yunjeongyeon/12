#12조 영단어 게임

score = 0

hard_kor = ['친절한', '후원하다', '교사','교육학', '평온한', '여러나라 말로 하는', '교훈', '선구자', '선배', '통찰']
hard_eng = ['propitious', 'patronize', 'pedagogue', 'pedagogy', 'placid', 'polyglot', 'precept', 'precursor', 'predecessor', 'prescience']
normal_kor = ['평화주의자', '기생충', '수동성의', '실제적인', '평화로운', '즉각적인', '사유의', '실행', '항의', '임신한']
normal_eng = ['pacifist', 'parasite', 'passive', 'pratical', 'peaceful', 'prompt', 'private', 'practice', 'protest', 'pregnant']
easy_kor = ['긍정적인', '공장', '열정', '자랑스러운', '잠재적인', '압박', '연극', '선호하다', '특정한', '성격']
easy_eng = ['possitive', 'plant', 'passion', 'proud', 'potential', 'pressure', 'play', 'prefer', 'particular', 'personality']
my_voca_kor = []
my_voca_eng = []



while True :

    print()
    print()
    print('메뉴를 선택하세요.')
    print('1. 영단어 수준 검사 게임')
    print('2. 나만의 단어장')


    menu = input('> ')

    if menu == '1' :
        print('안녕하세요. 당신의 영단어 수준을 알아볼 수 있는 게임에 참여하신 것을 환영합니다.')
        print()

        print('게임 방법: 난이도 선택 후, 보기에 있는 한글 뜻 중 하나를 골라 제시된 영단어에 입력해주세요.')
        print('*주의사항* 보기와 정확하게 일치하지 않을 경우 오답으로 처리됩니다.')
        print()

        print('게임의 난이도는 상(대학), 중(고등), 하(중등)로 나뉘어져있습니다. 자신의 영어실력을 고려하여 난이도를 선택해주세요.')
        print()

        print('상, 중, 하 중 난이도를 골라주세요.')
        choice = input('> ')

  
        if choice == '상' :
            print()
            
            print('==============================================================')
            print('<보기> 선구자, 후원하다, 교사, 통찰, 교육학, 평온한, 교훈, 여러나라 말로 하는, 선배, 친절한')
            print('==============================================================')
            print()
        
            for i in  range(len(hard_kor)) :
                print('\n', hard_eng[i], end='')
                print('는 무슨 뜻일까요?\n')
            
                ans1 = input('> ')
            
                if ans1 == hard_kor[i] :
                    print('정답!')
                    score += 1
                else :
                    print('땡! 이 단어의 뜻은', hard_kor[i], '이었습니다.')
                    print()

                    while True:
                        print('이 단어를 단어장에 추가하시겠습니까? (Y/N)')
                        ans2 = input('> ')
                        if ans2 == 'Y' :
                            print('이 단어를 단어장에 추가했습니다.')
                            my_voca_eng.append(hard_eng[i])
                            my_voca_kor.append(hard_kor[i])
                            print()
                            break
                        elif ans2 == 'N' :
                            break
                        else :
                            print('잘못된 값입니다. 다시 입력하세요.')

            


        elif choice == '중' :
            print()
            print('================================================================')
            print('<보기> 임신한, 수동성의, 실제적인, 실행, 평화로운, 즉각적인, 기생충, 사유의, 항의, 평화주의자')
            print('================================================================')
            print()
        
            for i in  range(len(normal_kor)) :
                print('\n', normal_eng[i], end='')
                print('는 무슨 뜻일까요?\n')
            
                ans1 = input('> ')
            
                if ans1 == normal_kor[i] :
                    print('정답!')
                    score += 1
                else :
                    print('땡! 이 단어의 뜻은', normal_kor[i], '이었습니다.')
                    print()

                    while True:
                        print('이 단어를 단어장에 추가하시겠습니까? (Y/N)')
                        ans2 = input('> ')
                        if ans2 == 'Y' :
                            print('이 단어를 단어장에 추가했습니다.')
                            my_voca_eng.append(normal_eng[i])
                            my_voca_kor.append(normal_kor[i])
                            print()
                            break
                        elif ans2 == 'N' :
                            break
                        else :
                            print('잘못된 값입니다. 다시 입력하세요.')
                        


        elif choice == '하' :
            print()
            print('==========================================================')
            print('<보기> 연극, 열정, 특정한, 자랑스러운, 공장, 잠재적인, 압박, 선호하다, 긍정적인, 성격')
            print('==========================================================')
            print()
        
            for i in  range(len(easy_kor)) :
                print('\n', easy_eng[i], end='')
                print('는 무슨 뜻일까요?\n')
            
                ans1 = input('> ')
            
                if ans1 == easy_kor[i] :
                    print('정답!')
                    score += 1
                else :
                    print('땡! 이 단어의 뜻은', easy_kor[i], '이었습니다.')
                    print()

                    while True:
                        print('이 단어를 단어장에 추가하시겠습니까? (Y/N)')
                        ans2 = input('> ')
                        if ans2 == 'Y' :
                            print('이 단어를 단어장에 추가했습니다.')
                            my_voca_eng.append(easy_eng[i])
                            my_voca_kor.append(easy_kor[i])
                            print()
                            break
                        elif ans2 == 'N' :
                            break
                        else :
                            print('잘못된 값입니다. 다시 입력하세요.')


            
        else :
            print('잘못된 값입니다. 다시 입력하세요.')



        print('당신의 점수는', score,'점입니다.')
        if score == 0 :
            print('노력이 부족하네요. 공부 좀 더 하세요!')



    elif menu == '2' :
        if len(my_voca_eng) == 0 :
            print('단어장에 단어가 없습니다.')
        else :
            print('======= <나만의 단어장> ======')
            for i in range(len(my_voca_eng)) :
                print(i+1,'. ', my_voca_eng[i],'  ', my_voca_kor[i]) 
            print('=========================')
        print()
        print('1. 단어 추가')
        print('2. 단어 삭제')
        print('3. 단어 수정')
        print('4. 단어장 종료')

        voca_choice = input('> ')
        
        if voca_choice == '1' :
            print('추가 할 영단어를 입력하세요.')
            voca_eng = input('> ')
            my_voca_eng.append(voca_eng)
            print()
            print('영단어의 뜻을 입력하세요.')
            voca_kor = input('> ')
            my_voca_kor.append(voca_kor)
            print('단어가 추가되었습니다.')
            print()
    
        elif voca_choice == '2' :
            print('======= <나만의 단어장> ======')
            for i in range(len(my_voca_eng)) :
                print(i+1,'. ', my_voca_eng[i],'  ', my_voca_kor[i])
            print('=========================')
            print()
            
            print('삭제할 영단어의 번호를 입력하세요.')
            ans = int(input('> '))
            if (ans <= len(my_voca_eng) and  ans > 0) :
                del my_voca_eng[ans-1] 
                del my_voca_kor[ans-1]
                print('삭제되었습니다.')
                print()

        elif voca_choice == '3' :
            print('======= <나만의 단어장> ======')
            for i in range(len(my_voca_eng)) :
                print(i+1,'. ', my_voca_eng[i],'  ', my_voca_kor[i])
            print('=========================')
            print()

            print('수정할 영단어의 번호를 입력하세요.')
            ans = int(input('> '))
            if (ans <= len(my_voca_eng) and  ans > 0) :
                print('수정할 영단어를 새로 입력하세요.')
                update_eng = input('> ')
                print('수정할 영단어의 뜻을 새로 입력하세요.')
                update_kor = input('> ')
                my_voca_eng[ans-1] = update_eng
                my_voca_kor[ans-1] = update_kor
                print('수정되었습니다.')
                print()

        else :
            print('단어장을 종료합니다.')
            
