import sandwiches_import
sandwiches_import.make_sandwich('cucumber')

from sandwiches_import import make_sandwich
make_sandwich('cheese')

from sandwiches_import import make_sandwich as ms
ms('mozarella')

import sandwiches_import as si
si.make_sandwich('tomato')

from sandwiches_import import *
make_sandwich('goat cheese')