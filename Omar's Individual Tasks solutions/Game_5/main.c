#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <unistd.h>
#include <string.h>

void rand_string(char *str, int num);
void shuffle_characters(char *s);

int main()
{
    // Give a random seed each time the program gets executed to the srand() function
    srand(time(NULL));
    int size = 20, flag = 0;
    int score_1 = 0, score_2 = 0, turn = 1;
    char tmp[size / 2], str[size];
    char screen[] = "Welcome: 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0\n";
    rand_string(tmp, size / 2);
    for (int i = 0; i < size / 2; i++)
        str[i] = tmp[i];
    shuffle_characters(tmp);
    for (int i = 0; i < size / 2; i++)
        str[i + size / 2] = tmp[i];
    shuffle_characters(str);
    for (int i = 0; i < size; i++)
        printf("%c ", str[i]);
    printf("\n");
    sleep(5);
    // Special string to clear the screen
    printf("\033[2J\033[1;1H");
    while (flag != size)
    {
        char c1, c2;
        int pos1, pos2, space1, space2;
        printf(screen);
        if (turn & 1)
        {
            printf("Player#%d-score %d: ", turn, score_1);
            scanf("%d %d", &pos1, &pos2);
            space1 = pos1 - 1, space2 = pos2 - 1;
            c1 = screen[pos1 + space1 + 8];
            screen[pos1 + space1 + 8] = str[pos1 - 1];
            c2 = screen[pos2 + space2 + 8];
            screen[pos2 + space2 + 8] = str[pos2 - 1];
            printf(screen);
            sleep(4);
            // Special string to clear the screen
            printf("\033[2J\033[1;1H");
            screen[pos1 + space1 + 8] = c1;
            screen[pos2 + space2 + 8] = c2;
            if (str[pos1 - 1] == str[pos2 - 1] && pos1 != pos2)
            {
                score_1++, screen[pos1 + space1 + 8] = screen[pos2 + space2 + 8] = '*';
                flag += 2;
            }
            turn *= 2;
        }
        else
        {
            printf("Player#%d-score %d: ", turn, score_2);
            scanf("%d %d", &pos1, &pos2);
            space1 = pos1 - 1, space2 = pos2 - 1;
            c1 = screen[pos1 + space1 + 8];
            screen[pos1 + space1 + 8] = str[pos1 - 1];
            c2 = screen[pos2 + space2 + 8];
            screen[pos2 + space2 + 8] = str[pos2 - 1];
            printf(screen);
            sleep(4);
            // Special string to clear the screen
            printf("\033[2J\033[1;1H");
            screen[pos1 + space1 + 8] = c1;
            screen[pos2 + space2 + 8] = c2;
            if (str[pos1 - 1] == str[pos2 - 1] && pos1 != pos2)
            {
                score_1++, screen[pos1 + space1 + 8] = screen[pos2 + space2 + 8] = '*';
                flag += 2;
            }
            turn /= 2;
        }
    }
    if (score_1 > score_2)
        printf("The winner is s 1\n");
    else if (score_2 > score_1)
        printf("The winner is s 2\n");
    else
        printf("Tie\n");
    return 0;
}

void rand_string(char *str, int num)
{
    for (int i = 0; i < num; i++)
    {
        char ch;
        do
        {
            ch = rand() % 26 + 'A';
        } while (strchr(str, ch) != NULL);
        str[i] = ch;
    }
}

// Fisher Yates shuffling algorithm
void shuffle_characters(char *s)
{
    int last_idx = strlen(s) - 1;
    while (last_idx)
    {
        int rand_idx = rand() % (last_idx);
        char ch = s[rand_idx];
        s[rand_idx] = s[last_idx];
        s[last_idx] = ch;
        last_idx--;
    }
}
