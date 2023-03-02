#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <unistd.h>

void rand_string(char *str, int len);
void shuffle_characters(char *s);

char all_chars[] = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

int main()
{
    // Give a random seed each time the program gets executed to the srand()
    // function
    srand(time(NULL));
    int size = 20, flag = 0;
    int score_1 = 0, score_2 = 0, turn = 1;
    char tmp[size / 2 + 1], str[size + 1];

    char screen[] = "Welcome: 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0\n";
    rand_string(tmp, (size / 2) + 1);
    strcpy(str, tmp);
    shuffle_characters(tmp);
    strncat(str, tmp, (size / 2) + 1);
    str[size] = 0;
    for (int i = 0; i < size; i++)
        printf("%c ", str[i]);
    printf("\n");
    sleep(5);
    // Special string to clear the screen
    printf("\033[2J\033[1;1H");
    for (; flag != size; turn = (turn & 1 ? 2 : 1))
    {
        char c1, c2;
        int pos1, pos2;
        printf("%s", screen);
        printf("Player#%d-score %d: ", turn, turn & 1 ? score_1 : score_2);
        scanf("%d %d", &pos1, &pos2);
        c1 = screen[2 * pos1 + 7];
        screen[2 * pos1 + 7] = str[pos1 - 1];
        c2 = screen[2 * pos2 + 7];
        screen[2 * pos2 + 7] = str[pos2 - 1];
        printf("%s", screen);
        sleep(4);
        // Special string to clear the screen
        printf("\033[2J\033[1;1H");
        screen[2 * pos1 + 7] = c1;
        screen[2 * pos2 + 7] = c2;
        if (str[pos1 - 1] == str[pos2 - 1] && pos1 != pos2)
        {
            screen[2 * pos1 + 7] = screen[2 * pos2 + 7] = '*';
            flag += 2;
            turn & 1 ? score_1++ : score_2++;
        }
    }

    if (score_1 > score_2)
        printf("The winner is Player 1\n");
    else if (score_2 > score_1)
        printf("The winner is Player 2\n");
    else
        printf("Tie\n");
    return 0;
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

void rand_string(char *s, int len)
{
    shuffle_characters(all_chars);
    strncpy(s, all_chars, len - 1);
    s[len - 1] = 0;
}
