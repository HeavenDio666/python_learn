import uuid

from openai import OpenAI

from Content.models import Option, Test


# client = OpenAI(
#     api_key="0ad31a37f185576579a1fd201b610379.mpv5pTFPrxyO2QC3",
#     base_url="https://open.bigmodel.cn/api/paas/v4/"
# )
#
# completion = client.chat.completions.create(
#     model="glm-4-air",
#     messages=[
#         {"role": "system", "content": "关于计算机的考试"},
#         {"role": "user",
#          "content": "生成一道单选题"}
#     ],
#     top_p=0.7,
#     temperature=0.9
# )
#
# print(completion.choices[0].message.content)


def generate(content, amount, _type):
    typeMap = {
        "0": "单选题",
        "1": "多选题",
        "2": "判断题",
    }
    type_name = typeMap[_type]
    client = OpenAI(
        api_key="0ad31a37f185576579a1fd201b610379.mpv5pTFPrxyO2QC3",
        base_url="https://open.bigmodel.cn/api/paas/v4/"
    )

    completion = client.chat.completions.create(
        model="glm-4-air",
        messages=[
            {"role": "system", "content": content},
            {"role": "user",
             "content": "生成" + str(amount) + "道" + type_name}
        ],
        top_p=0.7,
        temperature=0.9
    )
    print(completion.choices[0].message.content)
    _content = completion.choices[0].message.content.splitlines()
    index = 0
    _name = ""
    _optionA = ""
    _optionB = ""
    _optionC = ""
    _optionD = ""
    _optionE = ""
    for line in _content:
        print(line)
        if line is None or line == '':
            continue
        _line_list = line.split('.')
        if len(_line_list) == 1:
            _line_list = line.split('：')
            _answer = _line_list[1]
            index = 0
            _uuid = uuid.uuid4()
            Test.objects.create(
                uid=_uuid,
                name=_name,
                analysis=_name,
                answer=_answer,
                type=_type,
            )
            if _optionA is not None and _optionA != '':
                Option.objects.create(
                    uid=uuid.uuid4(),
                    name=_optionA,
                    choice='A',
                    seq=1,
                    test=_uuid,
                )
            if _optionB is not None and _optionB != '':
                Option.objects.create(
                    uid=uuid.uuid4(),
                    name=_optionB,
                    choice='B',
                    seq=2,
                    test=_uuid,
                )
            if _optionC is not None and _optionC != '':
                Option.objects.create(
                    uid=uuid.uuid4(),
                    name=_optionC,
                    choice='C',
                    seq=3,
                    test=_uuid,
                )
            if _optionD is not None and _optionD != '':
                Option.objects.create(
                    uid=uuid.uuid4(),
                    name=_optionD,
                    choice='D',
                    seq=4,
                    test=_uuid,
                )
            if _optionE is not None and _optionE != '':
                Option.objects.create(
                    uid=uuid.uuid4(),
                    name=_optionE,
                    choice='E',
                    seq=5,
                    test=_uuid,
                )
            continue
        _line = _line_list[1]
        if index == 0:
            _name = _line
        if index == 1:
            _optionA = _line
        if index == 2:
            _optionB = _line
        if index == 3:
            _optionC = _line
        if index == 4:
            _optionD = _line
        if index == 5:
            _optionE = _line
        index = index + 1


if __name__ == "__main__":
    try:
        # 在您的控制台的应用管理处获取
        generate("关于一级建造师", 3, "单选题")
    except Exception as e:
        print("except:", e)
